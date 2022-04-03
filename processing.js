

function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

let points=0
let highscore=0
let imageList=[]
let data={}
let stateColor="gray"
let countryColor="gray"
let cityColor="gray"
let count = 0
let hearts=0
let lives=3
let wait="on"


function onLoad(){
  document.getElementById("BackA").style.visibility = "hidden";
  document.getElementById("frontA").style.visibility = "hidden";
  document.getElementById("guess").style.visibility = "hidden";
  document.getElementById("guesses").style.visibility = "hidden";
  document.getElementById("conti").style.visibility = "hidden";
  document.getElementById("link").style.visibility = "hidden";
  document.getElementById("StartB").style.visibility = "hidden";
  document.getElementById("points").style.visibility = "hidden";
  document.getElementById("pText").style.visibility = "hidden";
  document.getElementById("hrt3").style.visibility = "hidden"
  document.getElementById("hrt2").style.visibility = "hidden"
  document.getElementById("hrt1").style.visibility = "hidden"
  document.getElementById("life").style.visibility = "hidden"
 setTimeout(function te() {
   document.getElementById("pic").src="https://i.imgur.com/hDyhMgg.png"
   wait="off"
   document.getElementById("StartB").style.visibility = "visible";
 },4000)
  
}

function next(){
    if(count < imageList.length-1){
        count+=1;
        document.getElementById("pic").src=imageList[count];
    }    else {
        count=0;
        document.getElementById("pic").src=imageList[count];
    }
}

function back(){
    if(count > 0){
        count-=1;
        document.getElementById("pic").src=imageList[count];
    }    else {
        count=imageList.length-1;
        document.getElementById("pic").src=imageList[count];
    }
}


function startingImage(response){
    imageList=JSON.parse(response)[1];
    data=JSON.parse(response)[0]
    count=0;
    document.getElementById("pic").src=imageList[count];
  document.getElementById("StartB").style.visibility = "hidden";
  document.getElementById("points").style.visibility = "visible";
  document.getElementById("pText").style.visibility = "visible";
}


function start(){
  if (wait=="off"){
  document.getElementById("BackA").style.visibility = "visible";
  document.getElementById("frontA").style.visibility = "visible";
  document.getElementById("guess").style.visibility = "visible";
  document.getElementById("guesses").style.visibility = "visible";
  document.getElementById("hrt3").style.visibility = "visible"
  document.getElementById("hrt2").style.visibility = "visible"
  document.getElementById("hrt1").style.visibility = "visible"
    document.getElementById("life").style.visibility = "visible"
  ajaxGetRequest("/image",startingImage);
  }
  
  
}

function stat(){
    document.getElementById("pic").src=imageList[count];
}

function guess() {
  document.getElementById("guess").style.visibility = "hidden";
  document.getElementById("conti").style.visibility = "hidden";
   document.getElementById("conti").style.visibility = "visible";
  document.getElementById("link").style.visibility = "visible";
  document.getElementById("BackA").style.visibility = "hidden";
  document.getElementById("frontA").style.visibility = "hidden";
  let city=document.getElementById("City").value
  let State=document.getElementById("State").value
  let Country=document.getElementById("Country").value
  let pointsLoc=document.getElementById("points").value
  
  console.log(points)
  console.log(data["city"])
  console.log(data["Country"])
  console.log(data["State"])
  if (city==data["city"]){
    points+=50
    document.getElementById("City").style.background = "Green";
  }else{
    hearts=1
    document.getElementById("City").style.background = "Red";
  }
  if (Country==data["Country"]){
    document.getElementById("Country").style.background = "Green";
    points+=20
  }else{
    document.getElementById("Country").style.background = "Red";
    hearts=1
  }
  if (State==data["State"]){
    document.getElementById("State").style.background = "Green";
    points+=30
  }else{
    document.getElementById("State").style.background = "Red";
    hearts=1
  }
  if(hearts>0){
    if (lives==3){ 
      document.getElementById("hrt1").style.visibility = "hidden";
      lives=lives-1
      hearts=0
      }else if(lives ==2){
        document.getElementById("hrt2").style.visibility = "hidden"
        lives=lives-1
        hearts=0
      }else if(lives == 1){
      document.getElementById("hrt3").style.visibility = "hidden"
        lives=lives-1
        hearts=0
        document.getElementById("pic").src="https://i.imgur.com/jAva9v1.png";
          if (highscore<points){
      highscore=points
    }
    document.getElementById("ns").innerHTML=points
    document.getElementById("hs").innerHTML=highscore
        document.getElementById("ns").style.visibility = "visible";
      document.getElementById("hs").style.visibility = "visible";
      
      }
      
  }
  pointsLoc=JSON.stringify(points)
  document.getElementById("points").innerHTML = pointsLoc;
  document.getElementById("link").href = data["url"];
  //document.getElementById("City").value = data["city"];
  //document.getElementById("Country").value = data["Country"];
  //document.getElementById("State").value = data["state"];
  
  
}
function conti() {
  if (lives==0){
    lives=3
    points=0
    document.getElementById("points").innerHTML = 0;
     document.getElementById("ns").style.visibility = "hidden";
      document.getElementById("hs").style.visibility = "hidden";
    document.getElementById("guess").style.visibility = "visible";
   document.getElementById("conti").style.visibility = "hidden";
  document.getElementById("BackA").style.visibility = "visible";
  document.getElementById("frontA").style.visibility = "visible";
  document.getElementById("hrt1").style.visibility = "visible"
  document.getElementById("hrt3").style.visibility = "visible"
  document.getElementById("hrt2").style.visibility = "visible"
  document.getElementById("link").style.visibility = "hidden";
  document.getElementById("City").style.background = "Gray";
  document.getElementById("Country").style.background = "Gray";
  document.getElementById("State").style.background = "Gray";
  ajaxGetRequest("/image",startingImage);}
   else {
  document.getElementById("guess").style.visibility = "visible";
   document.getElementById("conti").style.visibility = "hidden";
  document.getElementById("BackA").style.visibility = "visible";
  document.getElementById("frontA").style.visibility = "visible";
  document.getElementById("link").style.visibility = "hidden";
  document.getElementById("City").style.background = "Gray";
  document.getElementById("Country").style.background = "Gray";
  document.getElementById("State").style.background = "Gray";
  ajaxGetRequest("/image",startingImage);
}
  
}
