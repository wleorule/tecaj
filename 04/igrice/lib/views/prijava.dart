import 'package:flutter/material.dart';
import 'package:igrice/views/pocetni.dart';

class Prijava extends StatefulWidget {
  const Prijava({super.key});

  @override
  State<StatefulWidget> createState() {
    return PrijavaState();
  }
}

class PrijavaState extends State<Prijava> {
  void stisniGumb() {
    if (ctrlKorisnickoIme.text == "leo" && ctrlSifra.text == "12345") {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const PocetniEkran()),
      );
    } else {
      setState(() {
        formaNijeIspravna = true;
      });
    }
  }

  TextEditingController ctrlKorisnickoIme = TextEditingController();
  TextEditingController ctrlSifra = TextEditingController();

  bool formaNijeIspravna = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                "PRIJAVA",
                style: TextStyle(
                    fontSize: 32,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 20),
              ),
              const SizedBox(
                height: 32,
              ),
              if (formaNijeIspravna)
                const Text(
                  "Korisnicko ime ili sifra nisu ispravni!",
                  style: TextStyle(fontSize: 14, color: Colors.red),
                ),
              if (formaNijeIspravna)
                const SizedBox(
                  height: 12,
                ),
              TextField(
                controller: ctrlKorisnickoIme,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(
                height: 12,
              ),
              TextField(
                obscureText: true,
                controller: ctrlSifra,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(
                height: 12,
              ),
              SizedBox(
                width: double.infinity,
                height: 50,
                child: FilledButton(
                    onPressed: stisniGumb,
                    child: const Text(
                      "PRIJAVI SE",
                      style: TextStyle(
                          fontSize: 16,
                          letterSpacing: 8,
                          fontWeight: FontWeight.w500),
                    )),
              )
            ],
          ),
        ),
      ),
    );
  }
}
