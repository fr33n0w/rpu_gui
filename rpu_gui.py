import tkinter as tk
import requests
import json
import subprocess
import webbrowser
import threading

class GitHubPackageUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("Reticulum Package Updater GUI v1.2 by F")
        self.packages = [
            {'name': 'RNS', 'url': 'https://github.com/markqvist/Reticulum', 'owner': 'markqvist', 'repo': 'Reticulum'},
            {'name': 'LXMF', 'url': 'https://github.com/markqvist/lxmf', 'owner': 'markqvist', 'repo': 'lxmf'},
            {'name': 'NomadNet', 'url': 'https://github.com/markqvist/nomadnet', 'owner': 'markqvist', 'repo': 'nomadnet'},
            {'name': 'MeshChat', 'url': 'https://github.com/liamcottle/reticulum-meshchat', 'owner': 'liamcottle', 'repo': 'reticulum-meshchat', 'manual': True},
            {'name': 'Sideband', 'url': 'https://github.com/markqvist/Sideband', 'owner': 'markqvist', 'repo': 'Sideband', 'manual': True},
            {'name': 'RNode CE', 'url': 'https://github.com/liberatedsystems/RNode_Firmware_CE', 'owner': 'liberatedsystems', 'repo': 'RNode_Firmware_CE', 'manual': True}
        ]

        self.frame = tk.Frame(root, bg="#2b2b2b")
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Create a header frame
        header_frame = tk.Frame(self.frame, bg="#2b2b2b")
        header_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        tk.Label(header_frame, text="Package", font=("Helvetica", 11, "bold"), bg="#2b2b2b", fg="#ffffff").grid(row=0, column=0, columnspan=1, padx=0, pady=0, sticky="w")
        tk.Label(header_frame, text="Version", font=("Helvetica", 11, "bold"), bg="#2b2b2b", fg="#ffffff").grid(row=0, column=1,  columnspan=1, padx=32, pady=1, sticky="w")
        tk.Label(header_frame, text="Status", font=("Helvetica", 11, "bold"), bg="#2b2b2b", fg="#ffffff").grid(row=0, column=2,  columnspan=1, padx=6, pady=1, sticky="w")
        tk.Label(header_frame, text="Actions / Website", font=("Helvetica", 11, "bold"), bg="#2b2b2b", fg="#ffffff").grid(row=0, column=3, columnspan=2, padx=80, pady=1, sticky="w")

        self.app_name_labels = []
        self.latest_version_labels = []
        self.installed_labels = []
        self.github_buttons = []

        for i, package in enumerate(self.packages):
            app_name_label = tk.Label(self.frame, text=package['name'], font=("Helvetica", 10, "bold"), bg="#2b2b2b", fg="#ffffff")
            app_name_label.grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
            self.app_name_labels.append(app_name_label)

            latest_version_label = tk.Label(self.frame, text="", font=("Helvetica", 10, "bold"), bg="#2b2b2b", fg="#ffffff")
            latest_version_label.grid(row=i+1, column=1, padx=5, pady=5, sticky="w")
            self.latest_version_labels.append(latest_version_label)

            installed_label = tk.Label(self.frame, text="", font=("Helvetica", 10, "bold"), bg="#2b2b2b", fg="#ffffff")
            installed_label.grid(row=i+1, column=2, padx=5, pady=5, sticky="w")
            self.installed_labels.append(installed_label)

            if 'manual' in package:
                installed_label.config(text="Manual", fg="#66ccff")
                github_button = tk.Button(self.frame, text="Open GitHub Official Website ->>", font=("Helvetica", 10, "bold"), command=lambda package=package: self.open_github(package), bg="#4b4b4b", fg="#ffffff")
                github_button.grid(row=i+1, column=3, columnspan=3, padx=10, pady=5, sticky="w")
            else:
                install_update_button = tk.Button(self .frame, text="Install/Update ", font=("Helvetica", 10, "bold"), command=lambda package=package: self.install_update_package_thread(package), bg="#4b4b4b", fg="#ffffff")
                install_update_button.grid(row=i+1, column=3, padx=10, pady=1, sticky="w")

                github_button = tk.Button(self.frame, text="GitHub ->>", font=("Helvetica", 10, "bold"), command=lambda package=package: self.open_github(package), bg="#4b4b4b", fg="#ffffff")
                github_button.grid(row=i+1, column=4, padx=1, pady=1, sticky="w")

            self.github_buttons.append(github_button)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)

        # Create a footer frame
        footer_frame = tk.Frame(root, bg="#2b2b2b")
        footer_frame.pack(fill='x', padx=10, pady=10)

        self.check_updates_button = tk.Button(footer_frame, text="Check for Updates", font=("Helvetica", 12, "bold"), command=self.check_updates, bg="#4b4b4b", fg="#ffffff")
        self.check_updates_button.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        self.exit_button = tk.Button(footer_frame, text="Exit", font=("Helvetica", 12, "bold"), command=root.destroy, bg="#4b4b4b", fg="#ffffff")
        self.exit_button.pack(side='right', fill='x', expand=True, padx=5, pady=5)

        self.check_updates()

    def check_updates(self):
        for i, package in enumerate(self.packages):
            print(f"Checking updates for {package['name']}...")
            latest_version = self.get_github_version(package['owner'], package['repo'])
            if 'manual' not in package:
                installed_version = self.get_local_version(package['name'])
                if installed_version == latest_version:
                    self.installed_labels[i].config(text="Installed", fg="#33cc33")
                elif installed_version == "Not Installed":
                    self.installed_labels[i].config(text="Not Installed", fg="#ff0000")
                else:
                    self.installed_labels[i].config(text="Outdated", fg="#ff9900")
            self.latest_version_labels[i].config(text=latest_version)
            print(f"Finished checking updates for {package['name']}.")

    def get_github_version(self, owner, repo):
        api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()['tag_name']
        else:
            return "Error"

    def get_local_version(self, package_name):
        try:
            output = subprocess.check_output(['pip', 'show', package_name])
            return output.decode('utf-8').split('\n')[1].split(':')[1].strip()
        except subprocess.CalledProcessError:
            return "Not Installed"

    def install_update_package_thread(self, package):
        threading.Thread(target=self.install_update_package, args=(package,)).start()

    def install_update_package(self, package):
        print(f"Installing/Updating {package['name']}...")
        subprocess.call(['pip', 'install', '--upgrade', package['name']])
        print(f"Finished installing/updating {package['name']}.")
        self.check_updates()  # Call check_updates method to refresh the package list


    def open_github(self, package):
        webbrowser.open(package['url'])

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#2b2b2b")
    app = GitHubPackageUpdater(root)
    root.mainloop()