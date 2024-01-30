# Career_Harbor
## Stage-1 Front-End 
### Admin.html
#### Feedback Approved and Delete

###### 1.feedback_approval view -->Dynamic routing for approving feedback
###### 2.feedback_delete view -->Dynamic routing for delete feedback

### User data insert Form(User.html)

###### * Company Name  Input  name=c_name
###### * Company Link Input name=c_link


### Feedback form (index.html )
###### -Feedback Name Input name=f_name
###### -Feedback Rating Input name=f_rating
###### -Feedback Input name=feedback


## Stage-2 Database(Models)
## App Models
### Careers_hub--->Class name

| Attributes    | Models Fields | Constraints    |
| ------------- |:-------------:|---------------:|
| company_name  | CharField     | max_length=30  |
| company_link  | TextField     | max_length=100 |


### Career_Feedback--->Class name

|Attributes     | Models Fields   | Constraints                     | 
| --------------|:---------------:|--------------------------------:|
| fullname      | CharField()     | max_length=30                   |       
| email         | emailField()    |                                 |
| rating        | IntegerField()  |                                 |
| feedback      | CharField()     | max_length=500                  |
| status        | CharField()     | default="pending",max_length=20 |


## Stage-3 Backend 
### Main Urls---->
|   Route             |   App Name                    |
| --------------------|:-----------------------------:|
| ''                  | include('careers_web.urls')   |              

### App Views---->(Function names)
###### 1.home
###### 2.login_views
###### 4.admin_views
### App Urls ---->Function name with Nicknames


|   Route             |   Views Name            |   Nicknames                     | 
| --------------------|:-----------------------:|--------------------------------:|
| ''                  | views.home              |  name='career'                  |
| 'login'             | views.login_views       |  name='login'                   |    
|'AdminPanel'         | views.admin_views       |  name='AdminPanel'              |