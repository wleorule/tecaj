import 'dart:math';

import 'package:flutter/material.dart';

class SimonSays extends StatefulWidget {
  const SimonSays({super.key});

  @override
  State<SimonSays> createState() => _SimonSaysState();
}

class _SimonSaysState extends State<SimonSays> {
  BoxDecoration redBox = const BoxDecoration(color: Colors.red);
  BoxDecoration yellowBox = const BoxDecoration(color: Colors.yellow);
  BoxDecoration blueBox = const BoxDecoration(color: Colors.blue);
  BoxDecoration greenBox = const BoxDecoration(color: Colors.green);

  bool isPlaying = false;
  int currentlyPressed = 0;
  String title = "SIMON SAYS";

  void pressBox(int color, {bool fromPlay = false}) async {
    if (!isPlaying || fromPlay) {
      if (color == 0) {
        animateRed();
      } else if (color == 1) {
        animateBlue();
      } else if (color == 2) {
        animateYellow();
      } else if (color == 3) {
        animateGreen();
      }
    }
    if (!fromPlay) {
      if (popisBrojeva[currentlyPressed] == color + 1) {
        currentlyPressed++;

        if (currentlyPressed == popisBrojeva.length) {
          setState(() {
            title = "SIMON SAYS (${popisBrojeva.length})";
          });
          await Future.delayed(const Duration(milliseconds: 1500));
          play();
        }
      } else {
        showDialog(
            context: context,
            builder: (context) {
              return Material(
                  color: Colors.black26,
                  child: Container(
                    width: double.infinity,
                    height: double.infinity,
                    decoration:
                        BoxDecoration(borderRadius: BorderRadius.circular(20)),
                    child: Center(
                      child: Container(
                          padding: const EdgeInsets.all(20),
                          decoration: BoxDecoration(
                              color: Colors.white,
                              borderRadius: BorderRadius.circular(20)),
                          child: const Text("Izgubio si!")),
                    ),
                  ));
            });

        popisBrojeva = List.empty(growable: true);

        setState(() {
          title = "SIMON SAYS";
        });
      }
    }
  }

  List<int> popisBrojeva = List.empty(growable: true);
  Random random = Random();
  bool nastaviIgrat = true;

  void play() async {
    isPlaying = true;
    currentlyPressed = 0;
    popisBrojeva.add(1 + random.nextInt(4));

    for (var l in popisBrojeva) {
      pressBox(l - 1, fromPlay: true);
      await Future.delayed(const Duration(milliseconds: 1000));
    }

    isPlaying = false;
  }

  @override
  Widget build(BuildContext context) {
    double size =
        MediaQuery.of(context).size.width > MediaQuery.of(context).size.height
            ? MediaQuery.of(context).size.height * 0.5 - 60
            : MediaQuery.of(context).size.width * 0.5 - 60;

    size = size > 150 ? 150 : size;

    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.deepPurple.shade500,
          automaticallyImplyLeading: true,
          title: Text(
            title,
            style: const TextStyle(
                color: Colors.white,
                letterSpacing: 8,
                fontWeight: FontWeight.bold),
          ),
          actions: [
            IconButton(
                onPressed: play,
                icon: const Icon(
                  Icons.play_arrow_outlined,
                  color: Colors.white,
                )),
            IconButton(
                onPressed: () => print(1),
                icon: const Icon(
                  Icons.restart_alt_outlined,
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
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    GestureDetector(
                      onTap: () => pressBox(0),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        curve: Curves.easeOutExpo,
                        width: size,
                        height: size,
                        decoration: redBox,
                      ),
                    ),
                    const SizedBox(
                      width: 20,
                    ),
                    GestureDetector(
                      onTap: () => pressBox(1),
                      child: Container(
                        width: size,
                        height: size,
                        decoration: blueBox,
                      ),
                    )
                  ],
                ),
                const SizedBox(
                  height: 20,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    GestureDetector(
                      onTap: () => pressBox(2),
                      child: Container(
                        width: size,
                        height: size,
                        decoration: yellowBox,
                      ),
                    ),
                    const SizedBox(
                      width: 20,
                    ),
                    GestureDetector(
                        onTap: () => pressBox(3),
                        child: Container(
                          width: size,
                          height: size,
                          decoration: greenBox,
                        ))
                  ],
                )
              ]),
        ));
  }

  animateRed() {
    setState(() {
      redBox = BoxDecoration(color: Colors.red.shade700);

      Future.delayed(const Duration(milliseconds: 400)).then((_) {
        setState(() {
          redBox = const BoxDecoration(color: Colors.red);
        });
      });
    });
  }

  animateBlue() {
    setState(() {
      blueBox = BoxDecoration(color: Colors.blue.shade700);

      Future.delayed(const Duration(milliseconds: 400)).then((_) {
        setState(() {
          blueBox = const BoxDecoration(color: Colors.blue);
        });
      });
    });
  }

  animateYellow() {
    setState(() {
      yellowBox = BoxDecoration(color: Colors.yellow.shade700);

      Future.delayed(const Duration(milliseconds: 400)).then((_) {
        setState(() {
          yellowBox = const BoxDecoration(color: Colors.yellow);
        });
      });
    });
  }

  animateGreen() {
    setState(() {
      greenBox = BoxDecoration(color: Colors.green.shade700);

      Future.delayed(const Duration(milliseconds: 400)).then((_) {
        setState(() {
          greenBox = const BoxDecoration(color: Colors.green);
        });
      });
    });
  }
}
