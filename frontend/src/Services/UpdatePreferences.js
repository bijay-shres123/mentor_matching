import axios from 'axios'

export default function UpdatePreferences(preferences){
    var baseURL = `http://localhost:8000/api/preferences/`
    const options = {

        headers:{
          'Content-Type': 'application/json',
        }
    }
    var rank = 1
    for(let preference of preferences){
      console.log(rank)
        preference.rank = rank
        rank = rank + 1
        const Data = JSON.stringify(preference);
        let mainURL = baseURL + preference.id +"/"
   
        axios.put(mainURL ,Data, options )
        .then((responseJSON)=>{
          console.log(responseJSON)
        })
        .catch((error) => {
            if(error.response){
              
              console.log(error.response)
            }
            else if(error.request){
              console.log("2nd")
            }
            else{
    
              console.log('Err',error.message)
            }
          }
        )
    }
}