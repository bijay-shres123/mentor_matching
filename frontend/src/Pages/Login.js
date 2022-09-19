import LoginBox from "../Components/LoginBox"
import React from "react"
import { useEffect, useState } from 'react';

import {
  Navigate
} from "react-router-dom";
const Login = () => {
  const [userLoginInfo, setuserLoginInfo] = useState(false);

  useEffect(() => {
    if (localStorage.getItem('token')) {

      setuserLoginInfo(true);

    }
  }, []);
  if (userLoginInfo ===true){    
      return (
      <Navigate to ="/"/>
      )
}
  else{
  return(
   
   <LoginBox/>
  )   
  }
  }
  export default Login;