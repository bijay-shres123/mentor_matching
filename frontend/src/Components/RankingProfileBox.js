import React from "react";
import Table from 'react-bootstrap/Table';
import styled from 'styled-components';

const RankingProfileBox = () =>{
    return(
    <Wrapper className="container">
        <Table className="styledtable">
        <tr style={{'border':'2px solid #000'}}>
          <td>Mentor Name</td>
          <td>View Profile</td>
          
        </tr>
       
        </Table>
    </Wrapper>
    );
}

export default RankingProfileBox

const Wrapper = styled.div`

  font-size: 15px;
  line-height: 27px;
`;
