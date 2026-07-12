import { useEffect, useState } from "react";

import {
  FaLink,
  FaCheckCircle,
  FaExclamationTriangle,
  FaShieldAlt,
  FaBolt,
  FaBug,
  FaGlobe,
  FaLock
} from "react-icons/fa";

import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
} from "chart.js";

import { Pie, Bar } from "react-chartjs-2";

import "../styles/dashboard.css";
import "../styles/chart.css";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
);


function Dashboard() {


const [history,setHistory] = useState([]);



useEffect(()=>{

const data = JSON.parse(
localStorage.getItem("scanHistory")
) || [];


setHistory(data);


},[]);



const totalScans = history.length;


const safeUrls = history.filter(
(item)=>item.prediction !== "PHISHING"
).length;



const phishingUrls = history.filter(
(item)=>item.prediction === "PHISHING"
).length;

const chartData = {

labels:[
  "Safe URLs",
  "Phishing URLs"
],

datasets:[{

data:[
  safeUrls,
  phishingUrls
],

}]

};



const barData = {

labels:[
"Total Scans",
"Safe",
"Phishing"
],

datasets:[{

label:"URL Analysis",

data:[
totalScans,
safeUrls,
phishingUrls
]

}]

};

const averageConfidence = history.length > 0 ?

Math.round(
history.reduce(
(sum,item)=>sum + Number(item.confidence),
0
) / history.length
)

: 0;



return (

<div className="dashboard-container">


<h1>
Security Dashboard
</h1>


<p className="dashboard-subtitle">
Real-time AI phishing detection monitoring
</p>



<div className="stats-container">



<div className="stat-card">

<FaLink className="card-icon"/>

<div>

<h3>
Total Scans
</h3>

<p>
{totalScans}
</p>

</div>

</div>




<div className="stat-card safe">

<FaCheckCircle className="card-icon"/>

<div>

<h3>
Safe URLs
</h3>

<p>
{safeUrls}
</p>

</div>

</div>




<div className="stat-card danger">

<FaExclamationTriangle className="card-icon"/>

<div>

<h3>
Phishing Detected
</h3>

<p>
{phishingUrls}
</p>

</div>

</div>




<div className="stat-card">

<FaShieldAlt className="card-icon"/>

<div>

<h3>
Avg Confidence
</h3>

<p>
{averageConfidence}%
</p>

</div>

</div>



</div>





<div className="recent-section">


<h2>
Recent Scans
</h2>


<table>

<thead>

<tr>

<th>
URL
</th>

<th>
Status
</th>

<th>
Risk
</th>

</tr>

</thead>


<tbody>


{
history.slice(0,5).map(
(item,index)=>(

<tr key={index}>

<td>
{item.url}
</td>


<td className={
item.prediction==="PHISHING"
?
"danger-text"
:
"safe-text"
}>

{item.prediction}

</td>


<td>
{item.risk}
</td>


</tr>

)

)


}


</tbody>

</table>


</div>

<div className="charts-container">


<div className="chart-card">

<h2>
Threat Distribution
</h2>

<Pie data={chartData}/>

</div>



<div className="chart-card">

<h2>
Scan Statistics
</h2>

<Bar data={barData}/>

</div>


</div>

</div>

);

}


export default Dashboard;