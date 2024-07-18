import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuestionsView from '../views/QuestionsView.vue'
import EditQuestionView from '../views/EditQuestionView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionsView
    },
    {
      path: '/edit_question',
      name: 'edit_question',
      component: EditQuestionView,
      props: (route) => ({
        title: route.query.title,
        description: route.query.description,
        question_type: route.query.question_type,
        options: route.query.options ? JSON.parse(route.query.options) : [],
        option_biases: route.query.option_biases ? JSON.parse(route.query.option_biases) : {}
      })
    }
  ]
})

export default router
