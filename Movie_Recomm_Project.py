#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


#two datasets with same movie discription


# In[3]:


#*
movies = pd.read_csv("tmdb_5000_movies.csv")
movies.head(1)


# In[5]:


#*
credits = pd.read_csv("tmdb_5000_credits.csv")
credits.head(1)
#cast and crew required


# In[6]:


#need 1 dataset so we erger the 2 datasets into one
#we merger on teo basis movie( id or title)--title
#which want to.merge(with whom, on=' which basis')
#reassign it movies = 
#*
movies = movies.merge(credits,on='title')
movies

#get cast and crew from another table also


# In[7]:


#we delete the column we dont want to use 
#Need Content based Movie Recomm Sys -- so need tags for each movie
#Do the Columns helps me to create tage or not???
#ex1:- Column['budget'] -- we like the movie even if it would take huge amt. or tiny amt. to made., its depend on us
#so ['bugdet ']column is unnecessary/not usefull for us.
#ex2:-Column ['Genres'] -- it would help/usefull if you like the specfic type movie like sci-fi, horror , action,ect..
#ex3:- ["id"] -- helps us later when we make website ,we will Show poster, that's gonna fetch through id  
#ex4:- ["keywords"] -- tags
#ex5:- ["original language"] -- not need
#ex6:- ["original_title	"]  -- need 
#ex6:- ["overviews"] -- keep it , if we want to recc. movie acc. to content similarity to compare overview , if both movie have same summary then they are similar
#ex7:- ["popularity"] -- not use 
#ex8:- ["production_companies"] -- not play imp role, we dont reco.. movie acc. to this.
#ex9:- ["production_countries"] --   not matters
#ex10:-["release _date"] --  usefull( a little), some people like specific time period movie
#ex11:-["revenue"]      --  how much movie colected,  not usefull
#ex12:-["runtime"]      --   how log movie is , not matter
#ex12:-["spoken_language"]  - not matter
#ex14:-["status"]  -- reales ot upcoming , not matter 
#ex15:-["tagline	"]   -- is textual , what movie is or what is taglien is , not matter 
#ex16:-["title	"]   -- yessss
#ex17:-["vote_average"] --numerical , skip
#ex18:-["vote_count"]   --numerical , skip 
#ex19:-["movie_id"]   - noooo , we already take id 
#ex20:-["cast"]	      -- yessss
#ex21:-["crew"]	     -- yesss


# In[8]:


#movies.info()


# In[9]:


#We take
#genre, id, keywords, title,overviews, cast , crew

#now we take all the col. from table  , again stored in a movies
#*
movies = movies[['movie_id', 'title','overview','genres','keywords','cast','crew']]
movies.head(1)
#that's our main data we need to work with, we work on this now on 


# In[10]:


#we need to make a new dataframe from this dataframe
#and that contain 3 columns == movie's(movie_id , title , tags)
#[tags ]column made by merging( overview ,genres keywords,cast , crew)
#merging done == we take [overview] take add all [genres] into it,
#take [keywords] and add all into [overview + genre]
#cast - join top 3 cast , actors , i'll do recmmm. acco. to top 3 actors
#crew - join only Director name , i'll do recmmm. acco. to Dir. name

#at last I got a big para. , we need to take para. for each movie, we do so by :-
#1. preprocessing - get the col. in good format
#2. DataPreprossing - data cleaning, remove duplicate data and missing values
 


# In[11]:


# step1
#check the missing data and remove it
movies.isnull().sum()
#we have 3 missing values so not a ig deal


# In[12]:


#*drop the missing data and we see that now we dont have any missing values
movies.dropna(inplace=True)


# In[13]:


#check the dupliacted data and remove it

movies.duplicated().sum()

#we have 0 rows duplicates


# In[14]:


#step2 :- make the columns in a good format
#we take the 0th row of genre 
movies.iloc[0].genres

#now we see , its list of dictionaries and we need this in ['action' , 'adventure' ,' fantasy']


# In[15]:


#we need this dic.in the form of == ['Action' , 'Adventure' ,'Fantasy']
#we create a helper funtion
"""def convert(obj):
  l = []
  for i in obj:
    l.append(i['name'])
    return l
convert()    """ 
def convert(obj):
  l = []
  for i in ast.literal_eval(obj):
    l.append(i['name'])
  return l
#convert(obj)


# In[16]:


#in convert we pass object , inside of object we need to run a loop of list , we get 1 dictionary and from that dictionary 
#we take name (i['name]) and append this to the empty list (l)
#we got a problem== the list we get is a string not a int, if we call the fun. convert("[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]")
#we need to convert the string into integer, for that python has
import  ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')

#this helps to solve out the problem 
#we got a list 


# In[17]:


#we need to do that -- update def convert(obj)
# the obj we get is a string but ast.litearl_eval it convert into list
movies['genres'] = movies['genres'].apply(convert)

#we get all the genres of each movie in a list format


# In[18]:


#let us see what changes happend
movies.head() 


# In[19]:


movies.head(1)


# In[20]:


#*step 3:-  we do the same with keywords also , we manage then all togather
movies['keywords'] = movies['keywords'].apply(convert)


# In[21]:


#step4 :- Cast , top 3 actors
#from dic . we get into name and find 3 name
def convert3(obj):
  l=[]
  counter = 0
  for i in ast.literal_eval(obj):
    if counter !=3:
      l.append(i['name'])
      counter+=1
    else:
      break
  return l      


# In[22]:


movies['cast'] = movies['cast'].apply(convert3)


# In[23]:


movies.head(1)


# In[24]:


#step5 :- crew , only director can be used


# In[25]:


def convert4(obj):
  l=[]
  for i in ast.literal_eval(obj):
      if i['job']=='Director':
         l.append(i['name']) 
         break
  return l     


# In[26]:


movies['crew']=movies['crew'].apply(convert4)


# In[27]:


movies.head(1)


# In[28]:


#the[' overview'] col is also a string so i convert it to list
movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[29]:


movies.head(1)


# In[30]:


#we concatenate the list , formed a huge list and the convert inot a strings made a big para (tag columns)
#'sam vals' === 'samvals'
#both are dif words so sam is diff entity and vals also. both have diff tags
#so whenever we get anothe 'sam stat' so both have diff tags
#but both sam have diff tags so it find it difficult to read the actall one
# 


# In[31]:


movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
#we get no spaces 
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])


# In[32]:


movies.head(1)  # now no spaces in between the names


# In[33]:


# made a new columns named[tags] and append all thes columns into it
movies['tags'] = movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']


# In[34]:


movies.head(1)


# In[35]:


#make new datafreame
new_df = movies[['movie_id','title','tags']]


# In[36]:


new_df.head(1)


# In[37]:


#convert list (tags one) into string
new_df['tags']=new_df['tags'].apply(lambda x: " ".join(x))


# In[38]:


new_df.head(1)


# In[39]:


new_df['tags'][0]  #we get the entire column in a string format -- all col. in a single tag


# In[40]:


#*convert all string inot lower case, again stored inot new_df
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())


# In[41]:


#Vectoraization of text
#we have tags of all movies
#make a website , where user suggest a 5 movie related to that movie out of 5000 .similiarities based on tags
new_df['tags'][0]


# In[42]:


new_df['tags'][1]


# In[43]:


#TEXT VECTORIZATION
#how to find similarities between movies ??
#here we need vectorixation
#convert text[tags] into vector of 5000 movies
#so when i convert the each tags into vector then each movie is a vector
#5000 vectors so --- we take closed vector


# In[44]:


#tag1+tag2=tag_text
#1tag has 100 words so combined them and get 1000 words--mostly used words from tags


# In[45]:


#We use lib. SKLEARN
import sklearn
from sklearn.feature_extraction.text import CountVectorizer


# In[46]:


#creating a object
cv= CountVectorizer(max_features=5000,stop_words='english')
#need ==1. Max feature (tell the no. of words you need)
#2. Stop_Words (remove en words)


# In[47]:


#use object cv
vectors = cv.fit_transform(new_df['tags']).toarray()

#we get array as output
#.shape = tot movies
#we get each movie in vector form


# In[48]:


vectors[0]


# In[49]:


cv.get_feature_names()


# In[50]:


#Seaming = 
#ex:- [loving ,loved] ==> [love,love]
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
#obj of class

#helper fun
def stem(text):
  y=[]
  for i in text.split():
    y.append(ps.stem(i))

  return " ".join(y)  


# In[51]:


new_df['tags']=new_df['tags'].apply(stem)


# In[52]:


#ex:- 
#ps.stem('loved')  = love
#ps.stem('dancing') = dance


# In[53]:


stem('in the 22nd century, a paraplegic marine is dispatched to the moon pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. action adventure fantasy sciencefiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d samworthington zoesaldana sigourneyweaver jamescameron')


# In[54]:


#marine ==>marin


# In[55]:


#4806 mvoies ==> 4806 vectors->each vec. = 50000 no.
#each movie is vector
#we calculate distance(cosine)[find angle between two movie] of 1 movie with another  movie
#less distance , more similarities
#distance(cosine)[find angle between two movie] ==if angle is 5 close , 10 far , 180 opposite
#less the angle ,,more the similar

#to find the cosine distance between each movie to each movie , we have a fucntion  in sklearn (socine similarity)


# In[56]:


from sklearn.metrics.pairwise import cosine_similarity
#inverse of distance  1=more similarity or ==less smiliarity


# In[57]:


similarity = cosine_similarity(vectors)   #we pass the all vectors and cal. distance of each vector to eac vector


# In[58]:


#vector of (1st movie to 4806 movie) ,(2nd movie to 4806 movie) so on....

#* similarity[0]

#similairy of 1st movie with 1-4806 movie is 1.
#similairy of 1st movie with 2-4806 movie is 0.08.

#* list(enumerate(similarity[0])) 

#if we sorted the similarity matrix , the index postion is sorted so when before we re comparing the the index of 1st movie
#with all the movies ...after sorting all indexes are shuffle
#so we need to grap the indexex. the similarities 
#we call enumerate() function

#after we call enumerate function 

#list ==>list of tuples
#we get that 1st movie is with 2nd,3rd,4th...
#now apply sorting  
sorted(list(enumerate(similarity[0])), reverse=True,key=lambda x:x[1])[1:6]
#                                                                  take (5) movies from the list     


# In[59]:


sorted(similarity[0],reverse=True)
#sorting has been done


# In[60]:


#create a function called recommend if someone give me a movie then i reply with 5 similar movie 
#movie given then find index of the movies through wih we can move to similairty matric and then find the particular index movies.
#ill sort the index of the movie and return top 5 


# In[61]:


def recommend(movie):
  movie_index=new_df[new_df['title'] == movie].index[0]
  #i got index
  distances = similarity[movie_index]
  #index of similarity matrix
  movies_list=sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:7]

#print the list of movies , we get tuple

  for i in movies_list:
    #print(i[0])
    print(new_df.iloc[i[0]].title )
  return 
recommend('Avatar')  #fetch movie based on 
#sort the dictances  
#print(i) ==> give us movie_id 
#after that we get list of all movies 


# In[62]:


#new_df.iloc[1216].title  # we get a specific movie when we write the index 1216 we get from recommend('Movie_Name')


# In[65]:


recommend('Avatar')


# In[66]:


#Convert entire things into website


# In[71]:


import pickle


# In[73]:


pickle.dump(new_df,open('movies.pkl','wb'))
#we create a movies.pkl file in our folder, go to folder , copy path and paste it on pycharm  


# In[74]:


new_df['title'].values 


# In[70]:


pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))
#we create a movie_dict.pkl file in our folder, go to folder , copy path and paste it on pycharm 


# In[75]:


pickle.dump(similarity,open('similarity.pkl','wb'))  
#we create a similarity.pkl file in our folder, go to folder , copy path and paste it on pycharm  


# In[ ]:




