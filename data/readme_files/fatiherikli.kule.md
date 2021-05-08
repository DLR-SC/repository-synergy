### Simple REST Interface for MongoDB.

Kule is a REST interface for MongoDB. You can use kule as a temporary backend for your backend needed apps.

### Requirements

 - Bottle
 - Pymongo

### Installation

```sh
pip install kule
```

### Usage

```sh
python -m kule --database foo --collections users,documents
```

That's all. 

![Kule](http://i.imgur.com/OGeijqr.png)


Now you can interact with your API.


| Method        | Path          |           Action              |
| ------------- |---------------| ------------------------------|
| GET           | /users        | Returns all records. You can give limit and offset parameters to paginate records.     |
| GET           | /users/:id    | Returns a single document     |
| POST          | /users        | Creates a new document        |
| PUT           | /users/:id    | Replaces an existing document |
| PATCH         | /users/:id    | Updates a document            |
| DELETE        | /users/:id    | Removes an existing document  |



### Customization

You can customize your API response for your requirements.
For example, you can provide authentication method.

#### Example

You can override an existing endpoint.

```python
from kule import Kule

class MyKule(Kule):
    def delete_detail(self, collection, pk):
        return self.not_implemented()
```

#### Magical method names ...

You can override specific endpoint with kule's magical methods.

```python
from kule import Kule

class MyKule(Kule):
    def get_users_list(self, collection):
        return ["merhaba", "hello", "hola"]
```

#### Building custom bundle

Also there is a way to build customized bundles.

```python
from kule import Kule

class MyKule(Kule):
    def build_users_bundle(self, user):
        first_name, last_name = user.get("full_name").split()
        return {"first_name": first_name, 
                "last_name": last_name}
```

#### Starting app

```python
mykule = MyKule(database="foo")
mykule.run()
```

#### Using with Backbone.js

You have to override the parse method of collections. Because models listing
on `objects` key.

```javascript
Backbone.Collection.prototype.parse = function(data) {
    return data.objects ? data.objects : data;
};

// examples
var Document = Backbone.Model.extend({
    urlRoot: "http://localhost:8000/documents", // Supports CORS
    idAttribute: "_id"
});
var Documents = Backbone.Collection.extend({
    model: Document,
    url: "http://localhost:8000/documents"
});

// lets play
var _document = new Document({"title": "hello"});
_document.save()

_document.on('reset', function () {
    console.log(_document.id);
})
```
