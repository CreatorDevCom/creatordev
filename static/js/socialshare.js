 

/*

Social Share Links 
-> [Whatsapp]
-> [Facebook]
-> [Linkedin]
-> [Pinterest]
-> [Twitter]

  facebook -> https://www.facebook.com/sharer.php?u=[post-url]
  twitter ->  https://twitter.com/share?url={postUrl}&text={postTitle}
  pinterest -> https://pinterest.com/pin/create/bookmarklet/?media={postImg}&url={postUrl}&description={postTitle}
  whatsapp -> https://wa.me/?text={postTitle} {postUrl} 
  linkedin -> https://www.linkedin.com/sharerArticle?url={postUrl}&title={postTitle}

*/

let facebookBtn = document.querySelector('.facebook-btn');
let twitterBtn = document.querySelector('.twitter-btn');
let linkedinBtn = document.querySelector('.linkedin-btn');
let pinterestBtn = document.querySelector('.pinterest-btn');
let whatsappBtn = document.querySelector('.whatsapp-btn');

 
 
function share(postTitle , postImg){ 
  let postUrl = encodeURI(document.location.href)
  postTitle = encodeURI(postTitle)
  postImg = encodeURI(postImg) 



  facebookBtn.setAttribute(
    'href',
    `https://www.facebook.com/sharer.php?u=${postUrl}`
  )

  twitterBtn.setAttribute(
    'href',
    `https://twitter.com/share?url=${postUrl}&text=${postTitle}`
  )

  pinterestBtn.setAttribute(
    'href',
    `https://pinterest.com/pin/create/bookmarklet/?media=${postImg}&url=${postUrl}&description=${postTitle}`
  )

  whatsappBtn.setAttribute(
    'href',
    `https://wa.me/?text=${postTitle} ${postUrl} `
  )
    
  linkedinBtn.setAttribute(
  'href',
  `https://www.linkedin.com/sharerArticle?url=${postUrl}&title=${postTitle}`
  )

  


}
 