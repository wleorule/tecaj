import 'package:flutter/material.dart';

void main() {
  runApp(const PrviProgram());
}

class PrviProgram extends StatelessWidget {
  const PrviProgram({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            appBar: AppBar(
              backgroundColor: const Color(0xFF8e44ad),
              title: const Text(
                "Prijava",
                style: TextStyle(color: Colors.white, fontSize: 32),
              ),
              leading: IconButton(
                icon: const Icon(
                  Icons.menu_outlined,
                  color: Colors.white,
                ),
                onPressed: () => print("stisnut"),
              ),
              actions: [
                IconButton(
                  icon: const Icon(
                    Icons.favorite_outline,
                    color: Colors.white,
                  ),
                  onPressed: () => print("favorit"),
                ),
                IconButton(
                  icon: const Icon(
                    Icons.add_outlined,
                    color: Colors.white,
                  ),
                  onPressed: () => print("dodaj"),
                ),
              ],
            ),
            body: Expanded(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                mainAxisSize: MainAxisSize.max,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  const SizedBox(
                      width: double.infinity,
                      child: Text(
                        "PRIJAVA",
                        textAlign: TextAlign.center,
                        style: TextStyle(
                            color: Colors.black,
                            fontSize: 32,
                            fontWeight: FontWeight.bold),
                      )),
                  const Padding(
                      padding: EdgeInsets.symmetric(horizontal: 40),
                      child: TextField()),
                  const Padding(
                      padding: EdgeInsets.symmetric(horizontal: 40),
                      child: TextField()),
                  Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 40),
                      child: TextButton(
                        onPressed: () => print(1),
                        child: const Text("PRIJAVI ME"),
                      ))
                ],
              ),
            )));
  }
}
