const url = "http://localhost:5001"
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
function get_recommendations(payload){
    const queryString = new URLSearchParams(payload).toString();
    console.log(queryString)
    return get_data('/retrieve_customer_recommendations?' + queryString).then((data) => {
        return data
    })
}
export {get_data,get_questions, get_recommendations}