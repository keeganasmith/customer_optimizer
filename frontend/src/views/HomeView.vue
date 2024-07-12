<script setup>
import { onMounted, ref } from 'vue'
import { get_questions, get_recommendations } from '@/helper/requests'

let questions = ref([])
let question_results = ref([])
let loaded = ref(false)
let brands = ref([])
let packages = ref([])
onMounted(async() => {
  questions.value = await get_questions()
  question_results.value = questions.value.map(question => {
    let result = {};
    // Initialize each question type accordingly
    if (question.question_type === 'checkbox') {
      result[question.title] = []; // Initialize as an empty array for checkbox types
    } else if (question.question_type === 'number') {
      result[question.title] = 0.0; // Initialize as 0.0 for number types
    } else if (question.question_type === 'dropdown') {
      result[question.title] = ''; // Initialize as an empty string for dropdown types
    } else {
      result[question.title] = ''; // Default case for other types if necessary
    }
    return result;
  });
})
function submit(){
  let merged_results = Object.assign({}, ...question_results.value);
  (async () => {
    loaded.value = false
    let response = await get_recommendations(merged_results)
    brands.value = response["brands"]
    packages.value = response["packages"]

    loaded.value = true
  })()
}
</script>

<template>
  <h1>Outlet Optimization</h1>
  <ul>
    <li v-for="(question, index) in questions" :key="index">
      <h2>{{ question.title }}</h2>
      <p>{{ question.description }}</p>
      <template v-if="question.question_type === 'checkbox'">
        <ul>
          <li v-for="(option, optIndex) in question.options" :key="optIndex">
            <input type="checkbox" :id="'option-' + index + '-' + optIndex" :value="option" v-model="question_results[index][question.title]">
            <label :for="'option-' + index + '-' + optIndex">{{ option }}</label>
          </li>
        </ul>
      </template>
      <template v-if="question.question_type === 'number'">
        <input type="number" v-model="question_results[index][question.title]">
      </template>
      <template v-if="question.question_type ==='dropdown'">
        <select v-model="question_results[index][question.title]">
          <option v-for="(option, optIndex) in question.options" :key="optIndex" :value="option">
            {{ option }}
          </option>
        </select>
      </template>
    </li>
  </ul>
  <button @click="submit">Submit</button>
  <div v-if="loaded">
  <p><b>Brand Recommendations: </b> </p>
  <ul>
    <li v-for="(brand, index) in brands" :key="index">
      {{ brand[0] }}: Score of {{ brand[1] }}
    </li>
  </ul>
  <p><b>Package Recommendations</b></p>
  <ul>
    <li v-for="(packag, index) in packages" :key="index">
      {{ packag[0] }}: Score of {{ packag[1] }}
    </li>
  </ul>
  </div>
</template>