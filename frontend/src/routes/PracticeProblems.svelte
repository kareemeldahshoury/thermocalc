<script lang="ts">
  import { onMount } from 'svelte';
  
  type PracticeQuestion = {
    id: string;
    image: string;
    num_answers: number;
  };

  let question: PracticeQuestion | null = null;
  let userAnswers: string[] = [];
  let result: boolean[] = [];
  let showResult = false;

  async function loadQuestion() {
    showResult = false;
    const res = await fetch('http://localhost:8000/api/practice/random');
    question = await res.json();
    userAnswers = Array(question?.num_answers ?? 0).fill('');
    result = [];
  }

  async function submitAnswer() {
    if (!question) return;

    const payload = {
      id: question.id,
      answers: userAnswers.map((val) => parseFloat(val))
    };

    const res = await fetch('http://localhost:8000/api/practice/validate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    result = data.correct;
    showResult = true;
  }

  onMount(loadQuestion);
</script>

<div class="practice-container">
  {#if question}
    <div class="image-box">
      <img src={`http://localhost:8000${question.image}`} alt="Practice Problem" />
    </div>

    <div class="input-group">
      {#each userAnswers as ans, i}
        <input
          type="number"
          step="any"
          bind:value={userAnswers[i]}
          placeholder={`Answer ${String.fromCharCode(65 + i)}`}
        />
      {/each}
    </div>

    <button class="submit-btn" on:click={submitAnswer}>Check Answer</button>

    {#if showResult}
      <div class="results">
        {#each result as correct, i}
            <p>Answer {String.fromCharCode(65 + i)}: {correct ? '✅ Correct' : '❌ Incorrect'}</p>
        {/each}
        <button on:click={loadQuestion}>Try Another</button>
      </div>
    {/if}
  {/if}
</div>

<style>
.practice-container {
  max-width: 800px;
  margin: auto;
  padding: 30px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(0,0,0,0.1);
}

.image-box {
  text-align: center;
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
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 16px;
  justify-content: center;
}

input[type="number"] {
  padding: 8px 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  width: 120px;
}

.submit-btn {
  background: #7A0019;
  color: white;
  border: none;
  padding: 10px 18px;
  font-size: 1rem;
  border-radius: 6px;
  cursor: pointer;
  display: block;
  margin: 0 auto 20px auto;
}

.results {
  text-align: center;
  margin-top: 20px;
}

.results p {
  margin: 4px 0;
  font-size: 1rem;
}
</style>
