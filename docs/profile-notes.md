# Profile notes

Researched on 6 October 2026. This file documents the profile's wording and assets; it does not appear on the GitHub profile.

## Education

The profile owner supplied their student status, school, location and interest in application and web development. No graduation date, completed qualification, work experience, language proficiency or personal contact details were added.

[CFPT's training page](https://edurec.ge.ch/site/cfpt-informatique/metier-et-formations/) confirms its CFC application development pathway. [Its description of the profession](https://edurec.ge.ch/site/cfpt-informatique/metier-et-formations/le-metier-dinformaticien/) includes requirements analysis, application programming, quality, security and deployment.

[CFPT's formation plans](https://edurec.ge.ch/site/cfpt-informatique/communications/les-plans-des-formations/) identify different plans by cohort and training route. The [August 2024 dual plan](https://edurec.ge.ch/site/cfpt-informatique/wp-content/uploads/sites/115/2024/09/CFC-Developpement-dapplication-DUAL-aout-2024.pdf) describes the modular structure but does not enumerate a complete language list. The full-time PDF returned a server error during research.

## Technology selection

The seven language and web technology badges are a suggested learning roadmap, not a claim that every language is compulsory at CFPT or already mastered by the profile owner.

- [Mathias Orlandi's own account of his CFPT application/web development studies](https://www.malt.com/profile/mathiasorlandi) names C#, PHP, HTML and JavaScript.
- [Carlos's own account of his CFPT studies and programming tuition](https://www.superprof.fr/eleve-cfpt-informatique-3eme-annee-cours-programmation-python-javascript-php-sql-creation-site.html) names C#, Python, JavaScript, PHP and SQL.
- [Dany Serigado's own description of a CFPT school project](https://danyserigado.ch/) names HTML, CSS, PHP and SQL.

These first-person accounts support a relevant selection; they are not an official exhaustive syllabus. HTML and CSS are grouped as web technologies, and SQL as a query language. The roadmap can be adjusted to the owner's actual modules.

The profile owner subsequently confirmed proficiency in Docker, Git, NoSQL and Slim Framework, and requested their inclusion. These appear as confirmed skills in both the English and French introductions. No specific NoSQL product or additional unnamed skill was inferred. [Slim's official website](https://www.slimframework.com/) describes it as a PHP micro framework for web applications and APIs.

## Assets

The banner, animation, SQL and NoSQL symbols, Slim initial symbol, badge layouts and divider were made for this repository. All displayed images are local files, with no analytics, live stats widgets or external image-service dependency. The desktop and mobile animations are ordinary looping GIFs, with PNG alternatives for browsers requesting reduced motion.

The six language logos and the Docker and Git logos are from [Devicon](https://github.com/devicons/devicon), distributed under the MIT license. The license is preserved in `assets/badges/DEVICON-LICENSE.txt`. Product names and logos belong to their respective owners.

To regenerate the banner, install Pillow in your Python environment and run:

```sh
python scripts/generate_banner.py
```

To regenerate the badges, install requests in your Python environment and run `python scripts/generate_badges.py`. The Devicon source revision is pinned in the script.

For the GitHub profile, commit `README.md` together with the `assets` directory to the public `NorihyDev/NorihyDev` repository. The README's image paths are relative to that repository.
