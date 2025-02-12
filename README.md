Projet 2207 - Chatbot

Instance locale de Chroma DB sous Docker. Pourra être utilisé comme base de données vectorielle dans le cadre du développement d'un chatbot de soutien pour les utilisateurs de StudiUM.

Ce référentiel présente un exemple d'exécution du serveur Chroma DB dans un conteneur Docker, accessible à un autre service. 

Lien vers la documentation de chromadb : https://docs.trychroma.com/

Nous créons deux conteneurs. Un conteneur pour l'application qui agit comme client chroma et un conteneur pour le serveur de base de données chroma. Vous pouvez trouver les 2 services dans le fichier docker-compose.yml sous les noms « application » et « chroma ». Un pont est créé qui permet aux 2 services de communiquer.

Étapes à suivre pour que cela fonctionne :
Clonez le référentiel -> git clone https://github.com/sambapete/chroma-2207
Accédez au répertoire -> cd chroma-2207
Créez des conteneurs -> docker-compose up --build

Le script add_students_collection.py permet de tester l'installation d'une collection dans Chroma DB.

Le script check_persistence.py permet de tester la persistance des données après l'ajout d'une collection dans Chroma DB et le redémarrage du container dans Docker.

Le script chroma_client.py est un autre exemple de client permettant de se connecter à Chroma DB.

Le script chroma_client.py.non-mac-intel est le même script que le précédent mais ne fonctionne pas sur une plateforme Apple avec un processeur Intel.

Largement inspiré de https://github.com/abhitatachar2000/dockerize-chromadb et du Dockerfile et des fichers docker-compose.yml de https://github.com/chroma-core/chroma

Ne comprend pas encore d'instructions pour l'authentification ou l'authorisation au niveau de la base de données. A VENIR.
