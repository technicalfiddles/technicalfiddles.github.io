## My First *Real* Website


>"To do is to learn."


When I set out to build my own webpage, I began with the assumption that a customizable, easy to update website would require learning a significant amount of HTML. I wasn't clear on how domains interacted with hosting servers, or how you *actually* get your content on to the hosting server. So, I went with one of the many website wizards. The first website I ever built was through Neopets, but I didn't think that counted, so when it was time to build a real website, I used Squarespace. This was tedious, especially in sizing text boxes and getting the whole thing organized and layed out well. 

Fast forward a few years and I wanted to set up a blog to document progress on my sailboat restoration. This time, I had heard that a lot of bloggers used WordPress, so I investigated. Wordpress offerred all in one domain, hosting, and an editor, so I thought I had it made. I wrote a few posts with text interspersed with images and was happy with it until I realized all of my images still had personal metadata (GPS locations). I had forgotten to strip the metadata before uploading. Now I had about 30 images embedded in blog posts that I needed to somehow edit. Without a business pricing plan, I couldn't install Wordpress plugins to do this for me. The thought of re-uploading, sizing, captioning, and inserting each image back into the original blog post was too much for me so I sought another solution to build a website that is **easy** to update. 

Enter static sites. I can literally type things in a text editor on my computer, format them how I wish, link images (from a directory where I can edit the image any time I want), and then essentially hit upload (using git), and my page is live. 

Let's do this!

![porthole](media/img_6734.jpg# large)



<style type="text/css" rel="stylesheet">
body {background-color: rgb(0,0,0);
      color: rgb(255,255,255);}
h1 {color: rgb(255,200,200);}
h2 {color: rgb(255,150,150);}
h3 {color: rgb(255,100,100);}
p {color: rgb(255,255,255);}
img[src~="thumbnail"] {
   width:150px;
}
img[src~="bordered"] {
   border: 1px solid black;
}
img[src~="medium"] {
   width:350px;
}
img[src~="large"] {
   width:700px;
}
</style>