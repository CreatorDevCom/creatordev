 

  // <!-- Sec-head show  -->
  window.addEventListener('scroll', () => {
    let sec_header = document.getElementById('sec-header');
    sec_header.classList.toggle("active-sec-header", scrollY > 385) 
  })




  // Add like to comment
  const addliketocomment = async(commentId) =>{
  
    try {
        await fetch(`https://creatorsdev.herokuapp.com/article/likecomment/${commentId}`)
    } catch (error) {
      console.log(error);
    }
  }

  // Increment views on foucsing 
  const increseView =  async() =>{
    alert("Focused");
  }


  // Reply box active
  const replayActive = (id) => {
    var replay_box = document.getElementById(`replay-box${id}`);
    replay_box.classList.toggle('active-replay-box');

  }

  // Toggle (hide ,see) replies 
  const seeAllReplies = (id) => {
    document.getElementById(`rep-display-box${id}`).classList.toggle('activeDislpayReplies')
    let seeALlbtn = document.getElementById(`seeAll-btn${id}`)
    if (seeALlbtn.innerHTML == "see all") {
      seeALlbtn.innerHTML = "hide"
    } else {
      seeALlbtn.innerHTML = "see all"
    }
  }

  // Set h1 as a table of contetnts
  var article_body = document.getElementById("article-body");

  let h1 = article_body.querySelectorAll('h1')
  let tableOfContent = document.getElementById('tableofcontent');
  h1.forEach((item, ind) => {
    h1.item(ind).setAttribute("id", `${item.innerHTML}`)
    tableOfContent.innerHTML += ` 
    <a href="#${item.innerHTML}"><span  class="h1-contents">${ind + 1}. ${item.innerHTML}</span></a>
    `
  })

  // On Focus  h1
  h1.forEach((item, ind) => {
    item.addEventListener('focusin', () => {
      alert(ind);
    })
  })


  // Follow the user
  const addFollower = async (username) => { 
    try {
      await fetch(`https://creatorsdev.herokuapp.com/user/addfollower/${username}`)
    } catch (error) {
      console.log(error);
    }
  }



// Share To social Media