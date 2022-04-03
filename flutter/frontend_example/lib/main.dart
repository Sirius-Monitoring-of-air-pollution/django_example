import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: AddApp(),
    );
  }
}

class AddApp extends StatefulWidget {
  const AddApp({Key? key}) : super(key: key);

  @override
  State<AddApp> createState() => _AddAppState();
}

class _AddAppState extends State<AddApp> {
  int result = 0;

  final aValueController = TextEditingController();
  final bValueController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add app'),
      ),
      body: Column(children: [
        Text('A'),
        TextField(
          controller: aValueController,
        ),
        Text('B'),
        TextField(
          controller: bValueController,
        ),
        IconButton(
          icon: Icon(Icons.check),
          onPressed: () async {
            final Map<String, dynamic> body = {
              'a': int.parse(aValueController.value.text),
              'b': int.parse(bValueController.value.text),
            };
            final headers = {
              'Content-Type': 'application/json; charset=UTF-8',
            };
            final uri = Uri.http('localhost:8000', '/frontend_example/api/add');
            final res =
                await http.post(uri, headers: headers, body: jsonEncode(body));
            final resJson = jsonDecode(res.body);
            setState(() {
              result = resJson['result'];
            });
          },
        ),
        Text('Result: $result'),
      ]),
    );
  }
}
