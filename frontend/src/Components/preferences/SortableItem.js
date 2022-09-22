import React from 'react';
import { SortableElement } from 'react-sortable-hoc';
 
const SortableItem = (props) => {
  return <li class="list-group-item list-item-custom" style={{margin:'5px'}}>{props.value.candidate_addtional_profile.first_name} {props.value.candidate_addtional_profile.last_name}</li>
}
 
export default SortableElement(SortableItem);