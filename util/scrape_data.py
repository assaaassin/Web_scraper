from selenium import webdriver
import time
from util import *
#needed for doing actions like hover, click, drag and drop
AC = webdriver.common.action_chains
#the driver for firefox
browser = webdriver.Firefox();

#extracts genre of the cartoon (or any search)
def extract_data(search_query):

	browser.get("http://www.imdb.com/");	
	search_box = browser.find_element_by_id("navbar-query")
	AC.ActionChains(browser).move_to_element(search_box).click(search_box).perform();
	search_box.send_keys(search_query);
	search_enter = browser.find_element_by_id("navbar-submit-button");
	AC.ActionChains(browser).move_to_element(search_enter).click(search_enter).perform();
	#Wait till the above action has been performed (different for different internet speed)
	time.sleep(5);
	cartoon_title = browser.find_element_by_link_text(search_query);
	AC.ActionChains(browser).move_to_element(cartoon_title).click(cartoon_title).perform();
	#Wait till the above action has been performed (different for different internet speed)
	time.sleep(5);
	details = browser.find_element_by_class_name("subtext").text;
	genre = parse_genre(details);
	more = browser.find_element_by_class_name("show_more");
	AC.ActionChains(browser).move_to_element(more).click(more).perform();
	time.sleep(2)
	parental_guidance = browser.find_element_by_link_text("Parents Guide");
	AC.ActionChains(browser).move_to_element(parental_guidance).click(parental_guidance).perform();
	time.sleep(5);
	pg = browser.find_element_by_id("main").text;
	parents_guide = parse_pg(pg);

	cartoon_title = browser.find_element_by_link_text(search_query);
	AC.ActionChains(browser).move_to_element(cartoon_title).click(cartoon_title).perform();
	time.sleep(5)
	user_reviews = browser.find_element_by_link_text("USER REVIEWS");
	AC.ActionChains(browser).move_to_element(user_reviews).click(user_reviews).perform();
	time.sleep(5)
	all_reviews = browser.find_element_by_id("tn15content").text;
	# all_reviews = browser.find_element_by_tag_name("p").text;
	reviews_list = parse_reviews(all_reviews);
	return genre, parents_guide, reviews_list;
