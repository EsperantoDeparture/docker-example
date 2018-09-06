new_todo = {
  'type': 'string',
  'description': 'A new to do about to be added to the db',
  'properties': {
    'name': {
      'type': 'string',
      'description': 'Name of the todo',
      'example': 'Buy list'
    },
    'content': {
      'type': 'string',
      'description': 'Content of the todo',
      'example': 'A life'
    }
  }
}

todo = {
  'type': 'string',
  'description': 'A new to do about to be added to the db',
  'properties': {
    '_id': {
        'type': 'string',
        'description': 'A unique identifier for the todo',
        'example': '59c9d9019a892016ca4be412'
    },
    'name': {
      'type': 'string',
      'description': 'Name of the todo',
      'example': 'Buy list'
    },
    'content': {
      'type': 'string',
      'description': 'Content of the todo',
      'example': 'A life'
    }
  }
}
