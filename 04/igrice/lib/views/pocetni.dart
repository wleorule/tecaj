import 'package:flutter/material.dart';

class PocetniEkran extends StatelessWidget {
  const PocetniEkran({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.deepPurple.shade500,
          automaticallyImplyLeading: false,
          title: const Text(
            "IZBORNIK",
            style: TextStyle(
                color: Colors.white,
                letterSpacing: 8,
                fontWeight: FontWeight.bold),
          ),
          actions: [
            IconButton(
                onPressed: () => print(1),
                icon: const Icon(
                  Icons.favorite_outline,
                  color: Colors.white,
                )),
            IconButton(
                onPressed: () => print(1),
                icon: const Icon(
                  Icons.add_outlined,
                  color: Colors.white,
                ))
          ],
        ),
        body: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              TextButton(
                  onPressed: () => print(1),
                  child: const Text(
                    "Simon says",
                    style: TextStyle(fontSize: 18),
                  )),
              TextButton(
                  onPressed: () => print(1),
                  child: const Text(
                    "Memory",
                    style: TextStyle(fontSize: 18),
                  )),
              TextButton(
                  onPressed: () => print(1),
                  child: const Text(
                    "Tic tak toe",
                    style: TextStyle(fontSize: 18),
                  ))
            ],
          ),
        ));
  }
}
