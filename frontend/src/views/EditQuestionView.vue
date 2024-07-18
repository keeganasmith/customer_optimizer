<script setup>
import { questionStore } from '@/QuestionStore'
import {ref, onMounted} from 'vue'
import { get_question_types, get_brands, get_packages, update_question, remove_question } from '@/helper/requests';
//title = "", description = "", question_type = "", options = None, option_biases = None
let currentQuestion = questionStore.currentQuestion
let title = ref(currentQuestion.title)
let description = ref(currentQuestion.description)
let question_type = ref(currentQuestion.question_type)
let options = ref(currentQuestion.options)
let option_biases = ref(currentQuestion.option_biases)
let question_type_options = ref([])
let package_options = ref([])
let brand_options = ref([])
let loaded = ref(false)
let option_text = ref("")
onMounted(async() => {
    loaded.value = false
    question_type_options.value = await get_question_types()
    package_options.value = await get_packages()
    brand_options.value = await get_brands()
    loaded.value = true
})
function remove_option(option_name){
    console.log("option received was: " + option_name)
    loaded.value= false
    for(let i = 0; i < options.value.length; i++){
        if(options.value[i] === option_name){
            options.value.splice(i, 1);
            loaded.value = true
            break;
        }
    }
}
function add_option(){
    options.value.push(option_text.value)
    option_biases.value[option_text.value] = {}
    option_biases.value[option_text.value]["packages"] = {}
    option_biases.value[option_text.value]["brands"] = {}
    for(let i = 0; i < package_options.value.length; i++){
        option_biases.value[option_text.value]["packages"][package_options.value[i]] = 0
    }
    for(let i = 0; i < brand_options.value.length; i++){
        option_biases.value[option_text.value]["brands"][brand_options.value[i]] = 0
    }
    option_text.value = ""
}
async function save(){
    loaded.value = false
    await update_question(title.value, description.value, question_type.value, options.value, option_biases.value)
    loaded.value = true
}
</script>
<template>
    <div v-if="loaded">
        <div>
            <label for="title_input">Title:</label>
            <input type="text" v-model="title" id="title_input">
        </div>
        <div>
            <label for="description_input">Description:</label>
            <input type="text" v-model="description" id="description_input">
        </div>
        <div>
            <label for="question_type">Question Type:</label>
            <select v-model="question_type" id="question_type">
                <option v-for="(option, optIndex) in question_type_options" :key="optIndex" :value="option">
                    {{ option }}
                </option>
            </select>
        </div>
        <div>
            <p>Options</p>
            <ul>
                <li v-for="(option, optIndex) in options">
                {{ option }}
                <button @click="remove_option(option)">Remove</button>
                </li>
            </ul>
            <label for="new_option">Add a new option: </label>
            <input type = "text" id="new_option" v-model="option_text">
            <button @click="add_option">Submit</button>
        </div>
        <div>
            <p>Option Package Biases</p>
            <ul>
                <li v-for="(option, optIndex) in options">
                {{ option }}
                <ul>
                    <li v-for="(package_option, index) in package_options">
                        {{ package_option }}
                        <input type="number" v-model="option_biases[option]['packages'][package_option]">
                    </li>
                </ul>
                </li>
            </ul>
            <p>Option Brand Biases</p>
            <ul>
                <li v-for="(option, optIndex) in options">
                {{ option }}
                <ul>
                    <li v-for="(brand_option, index) in brand_options">
                        {{ brand_option }}
                        <input type="number" v-model="option_biases[option]['brands'][brand_option]">
                    </li>
                </ul>
                </li>
                </ul>
        </div>
        <button @click="save">Save Changes</button>
    </div>
</template>
<style scoped>
div {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  color: #fe001a; /* Coca-Cola Red */
  margin-bottom: 5px;
}

input[type="text"]{
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
}

button {
  background-color: #fe001a; /* Coca-Cola Red */
  color: white; /* White text */
  border: none;
  padding: 10px 20px;
  margin-top: 10px;
  font-size: 16px;
  border-radius: 5px;
}

button:hover {
  background-color: darkred; /* Darker shade for hover effect */
}


p {
  font-weight: bold;
  color: #fe001a; /* Coca-Cola Red */
}
</style>