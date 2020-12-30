# data-representation-project
Data representation and querying project

Lucia Saura

Table CRUD operations

<table>
<thead>
<tr>
<th>Action</th>
<th>Method</th>
<th>URL</th>
<th>Sample Params</th> 
<th>Sample Return</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get All</td>
<td>GET</td>
<td>/countries</td>
<td>none</td>
<td>[{...},{...},{...}]</td>  
</tr>
<tr>
<td>Find by id</td>
<td>GET</td>
<td>/countries/id</td>
<td>none</td>
<td>[{"id":"1","countryname":"xxx"},{"continent":"xxx","equalityrate":"xxx"}]
</td> 
<tr>
<td>Create</td>
<td>POST</td>
<td>/countries</td>
<td>{"countryname":"xxx"},{"continent":"xxx","equalityrate:"xxx"}</td>
<td>[{"id":"1","countryname":"xxx","continent":"xxx","equalityrate":"xxx"}]
</td>
</tr>
<tr>
<td>Update</td>
<td>PUT</td>
<td>/countries/id</td>
<td>{"equalityrate:"xxx"}</td>
<td>[{"id":"1","countryname":"xxx","continent":"xxx","equalityrate:"xxx"}]
</td>
</tr>
<td>Delete</td>
<td>DELETE</td>
<td>/countries/id</td>
<td>none</td>
<td>{"done:"true}
</td>
</tr>  
</tbody>
</table>

How to run the project. 

- Download the code from Github
- Please run the newtestDAO.py file
- Please run the server from the file called server.py
- Please find the web interface in countriesviewer2.hmtl
- Please open the countriesviewer2 page from the localhost url
- Please perform the create, getall, get by id, updte and delete operations 
