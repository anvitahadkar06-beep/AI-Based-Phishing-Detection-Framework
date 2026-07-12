import { useEffect, useState } from "react";
import { FaHistory } from "react-icons/fa";

import "../styles/history.css";


function History(){

const [history,setHistory] = useState([]);



useEffect(()=>{

const data = JSON.parse(
localStorage.getItem("scanHistory")
) || [];


setHistory(data);


},[]);



return(

<div className="history-container">


<h1>
<FaHistory/>
 Scan History
</h1>



<table>

<thead>

<tr>

<th>URL</th>

<th>Status</th>

<th>Risk</th>

<th>Confidence</th>

<th>Date</th>

</tr>

</thead>



<tbody>


{
history.length > 0 ?

history.map((item,index)=>(

<tr key={index}>


<td>
{item.url}
</td>


<td
className={
item.prediction==="PHISHING"
?
"danger-text"
:
"safe-text"
}
>

{item.prediction}

</td>


<td>
{item.risk}
</td>


<td>
{item.confidence}%
</td>


<td>
{item.date}
</td>


</tr>


))


:

<tr>

<td colSpan="5">

No scan history available

</td>

</tr>

}


</tbody>


</table>


</div>

);


}


export default History;