import {useState, useEffect} from "react"
import styled from 'styled-components'
import Card from "react-bootstrap/Card";
import { Button, Form, Alert } from "react-bootstrap"
import GetPreferences from '../Services/GetPreferences'
import UserBox from "./UserBox";
import { arrayMoveImmutable } from "array-move";
import SortableList from "./preferences/SortableList";
import SortableItem from "./preferences/SortableItem";
import UpdatePreferences from "../Services/UpdatePreferences"
import axios from 'axios'

const PreferenceContent = () => {
    const [Preference, setPreference] = useState([]);

    const onSortEnd = ({oldIndex, newIndex}) => {
        setPreference(prevItem => (arrayMoveImmutable(prevItem,oldIndex,newIndex)))
    }

    handleSubmit = ()=>{
        let token = localStorage.getItem('token');
        const options = {

            headers:{
              'Content-Type': 'application/json',
              "Authorization" : `Token ${token}`
            }
        }
        console.log("Creating Preferences")
        axios.get('http://127.0.0.1:8000/api/preferencecreate', options).then(()=>{
            GetPreferences().then((result)=>{
                if(result.status === 200){
                    
                    setPreference(result.data)
                    
                }
            })
        })
    }

    
    useEffect(() => {
        GetPreferences().then((result)=>{
            if(result.status === 200){
                
                setPreference(result.data)
                
            }
        })
      }, []);
      useEffect(() => {
        console.log(Preference)
        UpdatePreferences(Preference)
        }
      , [Preference]);

      function handleSubmit(e) {
        e.preventDefault();
        console.log(Preference)
    }
    return (
        <Wrapper>
        <div className="jumbotron" style={{background:'none'}}>
          <div className="container text-center text-lg-left">
            <div className="row justify-content-between">
                <div className='col-md-3'>
                    <div>
                    <Card style={{ width: '18rem' ,color:"#000" }}>
                    <Card.Img variant="top" src="assets/images/mentor.jpeg" className="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"/>
                    <Card.Body>
                        <Card.Title>Mr Mentee</Card.Title>
                        <Card.Text> 
                        <table class="table">
                        
                        <tbody>
                            
                            <tr>
                            <td>Course:</td>
                            <td>Bachelors of Computer Science</td>
                            
                            </tr>
                            <tr>
                            <td>Year:</td>
                            <td>First</td>
                            
                            </tr>
                            </tbody>
                            </table>
                        </Card.Text>
                    </Card.Body>
                    </Card>
                    </div>
                </div>
                <div className='col-md-8'>
                <div style={{marginTop:"20px"}}>
                    <Button 
                        className="btn btn-color px-5 mb-5 w-100"
                        style={{ marginTop: 30,BackgroundColor:'#40798C',color: '#fff' }}
                        variant="primary"
                        size="sm"
                        block type="submit"
                        onClick={handleSubmit}
                        >
                        Recommend Mentors
                    </Button>
                   
                    </div>
                <div>
                    <Card style={{ color:"#000" }}>
                    
                    <Card.Body>
                    <Card.Title style={{textAlign:"center"}}>Rank Your Preference</Card.Title>
                        <Card.Text> 
                        <table class="table">
                        <span style={{fontSize:'18px'}}>Please Drag and Drop to make your preference.</span>
                        <tbody class="list-group">
                        <SortableList items={Preference} onSortEnd={onSortEnd} />
                            </tbody>
                            </table>
                        </Card.Text>
                    </Card.Body>
                    </Card>
                    </div>
                    

                </div>
                </div>
                
              
            </div>
          </div>
        
      </Wrapper>)
  };
    
  export default PreferenceContent;
  const Wrapper = styled.section`
    margin-top:-25px;
  padding: 4em;
  min-height:700px;
  background-image: url(/assets/Images/background.jpg);
  background-size:cover;
  background-blend-mode: multiply;
  box-shadow: inset 0 0 0 2000px rgb(0 0 0 / 50%);
  color:#fff;
`;
