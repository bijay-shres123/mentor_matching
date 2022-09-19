import React,{Component,useEffect} from 'react'
import styled from 'styled-components'
import {Link} from 'react-router-dom'
import axios from 'axios'


export default class UserBox extends Component{
  constructor(props){
		console.log(props,"PROPS HO YO")
		super(props)
    this.state={
			message:"Hello",
			id:props.id,
            
		}

	}
	componentDidMount(){
		console.log(this.props,"props check")
	}
	
	

	render(){
        
  return(
	
				<>
					<td className="title-container">
						
						 {/* <img src={this.props.images.image} alt=""/>  */}
						<div className="title">
						<h4>{this.props.rank}</h4>
							
					    <span className="table-"> {this.props.candidate}</span>
						<span>Age: {this.props.candidate_additional_profile.age}</span>
					</div>
                    </td>
				</>

				

			
   

)
  }
}
const Wrapper = styled.div`
  font-size: 15px;
  line-height: 27px;
`;
