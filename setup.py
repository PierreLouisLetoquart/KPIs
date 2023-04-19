import subprocess

def install_dependencies():
    """
    Installe les dépendances à partir du fichier requirements.txt
    """
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des dépendances : {str(e)}")

if __name__ == "__main__":
    install_dependencies()
