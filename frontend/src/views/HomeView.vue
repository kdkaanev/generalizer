<script setup>

import { ref } from 'vue';
import axios from 'axios';


const url = ref('');
const summary = ref('');

const summarize = async () => {
  try {
    const response = await axios.post('http://localhost:8000/api/summarize/', {
      url: url.value
    });
    summary.value = response.data.summary;
  } catch (error) {
    console.error('Error summarizing the URL:', error);
    summary.value = 'Failed to summarize the URL.';
  }
};


</script>



<template>
  <div class="home">
    <h1>URL Summarizer</h1>
    <input v-model="url" type="text" placeholder="Enter URL to summarize" />
    <button @click="summarize">Summarize</button>
    <div v-if="summary">
      <h2>Summary:</h2>
      <p>{{ summary }}</p>
    </div>  

</div>
</template>