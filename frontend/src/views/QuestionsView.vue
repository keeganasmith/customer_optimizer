<script setup>
import {ref, onMounted} from 'vue'
import {get_questions, remove_question} from '@/helper/requests'
import { useRouter } from 'vue-router';
import { questionStore } from '@/QuestionStore'
let questions = ref([])
let loaded = ref(false)
const router = useRouter()
onMounted(async () => {
    loaded.value = false
    questions.value = await get_questions()
    loaded.value = true
})
function edit_question(question_title){
    let my_question = {}
    for(let i = 0; i < questions.value.length; i++){
        if(questions.value[i].title === question_title){
            my_question = questions.value[i]
            break;
        }
    }
    questionStore.currentQuestion = my_question
    router.push({
        name: 'edit_question'
    })
}
async function _remove_question(question_title){
    loaded.value = false
    await remove_question(question_title)
    questions.value = await get_questions()
    loaded.value = true
    
    
}
function new_question(){
    let title = "asdf"
    let description = ""
    let question_type = ""
    let options = []
    let option_biases = {}
    questionStore.currentQuestion = {
        title: title,
        description: description,
        question_type: question_type,
        options: options,
        option_biases: option_biases
    }
    router.push({
        name: 'edit_question',
    })
}
</script>
<template>
    <h1>Questions</h1>
    <button @click="new_question">Create a new question</button>
    <div v-if="loaded" v-for="(question, index) in questions" :key="index">
        <button @click="edit_question(question.title)">{{ question.title }}</button>
        <button @click="_remove_question(question.title)">x</button>
    </div>
</template>
<style scoped>
h1 {
  color: #fe001a; /* Coca-Cola Red */
  text-align: center;
}

button {
  background-color: #fe001a; /* Coca-Cola Red */
  color: white; /* White text */
  border: none;
  padding: 10px 20px;
  margin: 5px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 5px;
}

button:hover {
  background-color: darkred; /* Darker shade for hover effect */
}

div {
  text-align: center;
  margin-top: 20px;
}

div button {
  margin: 10px; /* Margin between buttons inside the div */
}

div button:last-child {
  background-color: black; /* Black button for remove */
}

div button:last-child:hover {
  background-color: darkgray; /* Darker shade for hover effect */
}
</style>