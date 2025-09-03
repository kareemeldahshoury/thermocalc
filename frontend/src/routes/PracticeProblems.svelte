<script lang="ts">


 type PracticeQuestion = {
  id: string;
  num_answers: number;
  image?: string;
  prompt?: string;
  format?: 'text' | 'image' | 'unknown';
  prompt_title?: string;
  prompt_body?: string
};


  let availableUnits = [
    { id: 'unitConversion', label: 'Unit Conversion / First Law' },
    { id: 'sysProperties', label: 'Properties of Systems'},
    { id: 'secondLaw', label: 'Second Law & Entropy' },
    { id: 'refrigeration', label: 'Refrigeration / Heat Engines' }
  ];

  let selectedUnit: string | null = null;
  let questionIds: string[] = [];
  let completedIds: string[] = [];
  let question: PracticeQuestion | null = null;
  let userAnswers: string[] = [];
  let result: boolean[] = [];
  let showResult = false;
  let completed = false;

  function allCorrect(): boolean {
    return result.length > 0 && result.every((r) => r === true);
  }

  async function selectUnit(unitId: string) {
    selectedUnit = unitId;
    completed = false;
    completedIds = [];
    questionIds = [];

    const res = await fetch(`http://localhost:8000/api/practice/list_ids?unit=${unitId}`);
    const data = await res.json();

    if (data.error) {
      alert(data.error);
      return;
    }

    questionIds = [...data.ids];
    loadQuestion();
  }

  async function loadQuestion() {
  showResult = false;

  if (questionIds.length === 0) {
    if (completedIds.length === 0) {
      alert("No questions available.");
      return;
    }
    completed = true;
    return;
  }

  completed = false;

  const nextId = questionIds.shift();
  if (!nextId) return;

  const res = await fetch(`http://localhost:8000/api/practice/get_by_id?id=${nextId}&unit=${selectedUnit}`);
  const data = await res.json();

  if (data.error) {
    alert(data.error);
    return;
  }

  question = data;
  userAnswers = Array(data.num_answers).fill('');
  result = [];

  completedIds.push(nextId);
}


function startOver() {
  questionIds = [...completedIds];
  completedIds = [];
  completed = false;
  loadQuestion();
}



  async function submitAnswer() {
    if (!question || !selectedUnit) return;

    const payload = {
      unit: selectedUnit,
      id: question.id,
      answers: userAnswers.map((val) => parseFloat(val))
    };

    const res = await fetch('http://localhost:8000/api/practice/validate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (data.error) {
      alert(data.error);
      return;
    }

    result = data.correct;
    showResult = true;
  }

  function skipQuestion() {
  if (!question) return;

  questionIds.push(question.id);

  loadQuestion();
}


  function backToUnits() {
    selectedUnit = null;
    question = null;
    result = [];
    userAnswers = [];
    showResult = false;
    completed = false;
    questionIds = [];
    completedIds = [];
  }
</script>

<div class="practice-container">
  {#if !selectedUnit}
    <h2 style="font-weight: bold;">Select a Unit</h2>
    <div class="unit-buttons">
      {#each availableUnits as unit}
        <button on:click={() => selectUnit(unit.id)}>{unit.label}</button>
      {/each}
    </div>
  {:else if completed}
  <div class="completed-message">
    <h2> You've completed all available questions for this unit!</h2>
    <button class="start-over-btn" on:click={startOver}>Start Over</button>
    <button class="back-btn" on:click={backToUnits}>Back to Units</button>
  </div>

  {:else if question}
    <div class="top-bar">
      <h2>{availableUnits.find(u => u.id === selectedUnit)?.label} Practice</h2>
      <button class="back-btn" on:click={backToUnits}>Back to Units</button>
    </div>

    <div class="question-box">
      {#if question?.prompt}
        <div class="prompt">{@html question.prompt}</div>
      {/if}

      {#if question?.image}
        <div class="image-box">
          <img src={`http://localhost:8000${question.image}`} alt="Practice Problem" />
        </div>
      {/if}
    </div>






    <div class="input-group">
      {#each userAnswers as _, i}
        <input
          type="number"
          step="any"
          bind:value={userAnswers[i]}
          placeholder={`Answer ${String.fromCharCode(97 + i)}`}
          class:selected-correct={showResult && result[i] === true}
          class:selected-incorrect={showResult && result[i] === false}
          disabled={showResult}
        />
      {/each}
    </div>

  {#if !showResult}
    <div class="button-row">
      <button class="skip-btn" on:click={skipQuestion}>Skip Question</button>
      <button class="submit-btn" on:click={submitAnswer}>Check Answer</button>
    </div>
  {:else if !allCorrect()}
    <div class="button-row">
      <button class="skip-btn" on:click={skipQuestion}>Skip Question</button>
      <button class="submit-btn" on:click={() => (showResult = false)}>Try Again</button>
    </div>
  {/if}

  {#if showResult}
    <div class="results">
      {#if allCorrect()}
        <button on:click={loadQuestion}>Try Another</button>
      {/if}
    </div>
  {/if}

  {/if}
</div>

<style>
  :global(body) {
    background-color: #f4f4f4;
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
  }

  .practice-container {
    position: relative;
    max-width: 800px;
    margin: -10px auto;
    padding: 30px 30px 35px 30px;
    background-color: white;
    color: #000;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    font-family: system-ui, sans-serif;
  }

  h2 {
    text-align: center;
  }

  .unit-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    margin-top: 30px;
  }

  .unit-buttons button,
  .results button {
    padding: 10px 20px;
    background-color: #7A0019;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
  }

  .back-btn {
    padding: 5px 10px;
    margin-top: 8px;
    background-color: #7A0019;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: .8rem;
    cursor: pointer;
  }
  

  .unit-buttons button:hover,
  .submit-btn:hover,
  .back-btn:hover,
  .results button:hover {
    background-color: #9c0033;
  }

  .top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .top-bar h2 {
    color: black;
    margin: 0;
    font-weight: bold
  }

 .image-box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 24px;
}


  .image-box img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ccc;
    border-radius: 8px;
  }

.input-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 16px;
}


  input[type="number"] {
    padding: 8px 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    width: 120px;
  }

  input.selected-correct {
    border: 1px solid green;
    background-color: #e6ffed;
  }

  input.selected-incorrect {
    border: 1px solid red;
    background-color: #ffe6e6;
  }

  .results {
    text-align: center;
  }

  .completed-message {
    text-align: center;
    margin-top: 20px;
    min-height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .completed-message h2 {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
}


  .start-over-btn {
    padding: 10px 20px;
    background-color: #7A0019;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
    margin-top: 40px;
    margin-right: 30px
}
.start-over-btn:hover {
  background-color: #9c0033;
  
}

.practice-container h2 {
  text-align: center;
  font-size: 1.5rem;
  font-weight: 700;
  
}

.prompt {
  white-space: pre-wrap;
  padding: 16px;
  font-size: 1rem;
  line-height: 1.4;
  margin-bottom: 24px;
  text-align: center;
  border: none;
  background: transparent;
  border: 1px solid #ccc;
  border-radius: 10px
}

.button-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.skip-btn,
.submit-btn {
  padding: 10px 20px;
  background-color: #7A0019;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
}

.skip-btn:hover,
.submit-btn:hover {
  background-color: #9c0033;
}

.question-box {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 5px;
  margin-bottom: 24px;
  background: white;
}

.prompt {
  white-space: pre-wrap;
  font-size: 1rem;
  line-height: 1.4;
  margin-bottom: 5px;
  text-align: center;
  border: none;
}

.image-box {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-box img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: none;
}





</style>
