
import axios from 'axios';


export default function GetPreferences() {
    let token = localStorage.getItem('token');
  const options = {

    headers:{
      'Content-Type': 'application/json',
      "Authorization" : `Token ${token}`

    }
  }

//   const Data = JSON.stringify();
  
  return new Promise((resolve) => {
   
    axios.get(`http://localhost:8000/api/preferences/`,options )
    .then((responseJSON)=>{
        
        
        resolve(responseJSON)
    })
    .catch((error) => {
        if(error.response){
            
          resolve(error.response)
        }
        else if(error.request){
          console.log("2nd")
        }
        else{
            
          console.log('Err',error.message)
        }
      }
    )
     
  });
}
