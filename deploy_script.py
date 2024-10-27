import os
import subprocess

def deploy_app():
    print("Starting deployment..")
    os.chdir(r'C:\Users\kelvi\OneDrive\Desktop\projects\Automated_Deployment_Script')
    subprocess.run(['git', 'pull'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    #subprocess.run(['systemctl', 'restart', 'myapp'])
    print("Restart command skipped on Windows.")
    print("Deployment is completed successfully!")





if __name__ == "__main__":
    deploy_app()
