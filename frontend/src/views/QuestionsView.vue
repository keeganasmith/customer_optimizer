<script setup>
import {ref, onMounted} from 'vue'
import {get_questions} from '@/helper/requests'
let questions = []
onMounted(async () => {
    questions = await get_questions()
    
})
</script>
<template>
    <h1>Questions</h1>
</template>