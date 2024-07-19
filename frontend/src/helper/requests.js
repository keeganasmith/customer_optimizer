const url = "https://customer-optimizer-66e490af52f5.herokuapp.com"
function get_data(endpoint){
    return fetch(url + endpoint, {
        method: 'GET'
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        return data
    })
}
function get_questions(){
    return get_data('/retrieve_questions').then((data) => {
        return data
    })
}
function get_question_types(){
    return get_data('/retrieve_question_types').then((data) => {
        return data
    }) 
}
function get_recommendations(payload){
    const queryString = new URLSearchParams(payload).toString();
    return get_data('/retrieve_customer_recommendations?' + queryString).then((data) => {
        return data
    })
}
function get_brands(){
    return get_data('/get_brand_options').then((data) => {
        return data
    })
}
function get_packages(){
    return get_data('/get_package_options').then((data) => {
        return data
    })
}
async function update_question(title, description, question_type, options, option_biases){
    let body = {
        title: title,
        description: description,
        question_type: question_type,
        options: options,
        option_biases: option_biases
    }
    body = JSON.stringify(body)
    try {
        let response = await fetch(url + '/create_or_edit_question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: body 
        })
        let data = await response.json()
        return data
    }
    catch(error){
        console.error('Errror:', error)
    }
}
async function remove_question(title){
    let body = {
        title: title
    }
    body = JSON.stringify(body)
    try{
        let response = await fetch(url + '/remove_question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: body
        })
        let data = await response.json()
        return data
    }
    catch(error){
        console.error("Error:",error)
    }
}
export {get_data,get_questions, get_recommendations, get_question_types, get_brands, get_packages, update_question, remove_question}