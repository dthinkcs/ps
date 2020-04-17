 

// percent_users who gate a star rating of 3.5 or higher is more than or equal to 60
if (percent_users >= 60) 
{
    // change the src of the imgae to fresh.jpg
    document.getElementById("rotten").src = "fresh.jpg";
} 
else  // percent_users who gate a star rating of 3.5 or higher is less than 60
{
    // change the src of the imgae to fresh.jpg
    document.getElementById("rotten").src = "rotten.jpg";
}



