import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Pages/Layout";
import Home from "./Pages/Home";
import MyProfile from "./Pages/MyProfile";
import Login from "./Pages/Login";
import SignUp from "./Pages/SignUp";
import UserDetails from "./Pages/UserDetails";
import Ranking from "./Pages/Ranking";
import Preference from "./Pages/Preference"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/login" element={<Login/>}/>
          <Route path="/myprofile" element={<MyProfile/>}/>
          <Route path="/signup" element={<SignUp/>}/>
          <Route path="/userdetails" element={<UserDetails/>}/>
          <Route path ="/ranking" element={<Ranking/>}/>
          <Route path ="/preference" element={<Preference/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));