clear 

printf "\n ________HUMDAN'S INTERVIEW TEST FOR GREY________\n\n"
printf "\tSelect from the Options Below:\n"
  
printf "(1) - What was the largest city, town, and village in each year?\n" 
printf "(2) - What are the three fastest growing cities in Texas between 2012-2016?\n"
printf "(3) - Which county had the most population in each year?\n" 
printf "(4) - Which county experienced the most growth in population over the timespan?\n" 
printf "(5) - Which county experienced the highest rate of growth from 2014-2016?\n" 
printf "(6) - What percentage of Texans lived in towns in 2017?\n" 
printf "(7) - Which year did Texas grow the most?\n"
printf "(0) - Contact Humdan\n\n"
printf ": "

read n
case $n in
    
    1)	printf "(1) - What was the largest city, town, and village in each year?\n" ;;
	2)	printf "(2) - What are the three fastest growing cities in Texas between 2012-2016?\n";;
	3)	printf "(3) - Which county had the most population in each year?\n";;
	4)	printf "(4) - Which county experienced the most growth in population over the timespan?\n" ;;
	5)	printf "(5) - Which county experienced the highest rate of growth from 2014-2016?\n" ;;
	6)	printf "(6) - What percentage of Texans lived in towns in 2017?\n" ;;
	7)	printf "(7) - Which year did Texas grow the most?\n\n";;
	0)	printf "Phone - 469 463 6843\n"
		printf "Email - Humdan.b@gmail.com\n\n";;

    *) invalid option;;
esac

$shell
