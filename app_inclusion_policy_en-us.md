# 📜 App Submission Policy (Aethra)

Welcome to **Aethra**. Our mission is to provide a modern, secure, and frictionless catalog of open-source Android apps.

Unlike other traditional repositories that have extremely strict rules about what constitutes a "pure" app or that require compiling everything from scratch, we take a **pragmatic** approach. We believe in free software, but also in modern technologies.

Below, we detail our criteria for accepting an app into Aethra:

## ✅ 1. Open Source
The app **must** have its source code published under a recognized free or open-source license (GPL, MIT, Apache, etc.). The repository must be publicly accessible (e.g., on GitHub or GitLab).

## 🤖 2. AI and External APIs Welcome!

We understand that modern software connects with the world.

- **Yes, we allow** applications that use third-party APIs (both free and commercial).

**Yes, we allow** AI-based applications (LLM clients, image generators, cloud service integrations, etc.).
We will not flag your app as "Anti-Feature" for connecting to non-free network services. We embrace innovation!

## 📦 3. APK Extraction (GitHub Releases)
To maintain fast updates and respect the developer's work, **we do not compile applications from source code**.

- We take pre-compiled `.apk` files directly from the **Releases** section of your repository.

- Make sure you upload your APKs there. If your app does not provide APKs in the releases, we will not be able to include it automatically.

## 🛡️ 4. Security and Analysis (VirusTotal)
Freedom does not have to come at the expense of security. To protect our users:
- Every APK indexed in Aura Repo will be scanned using the **VirusTotal** API.

- If the scan detects consistently malicious behavior (malware, Trojans, actual spyware), the application will be rejected or removed from the repository immediately.

- False positives from a couple of minor engines may be reviewed manually, but we reserve the right not to include suspicious applications.

## 🚫 5. What we DO NOT allow
While we are very flexible, there are logical limits. Applications that do not:
- Contain or promote malware, phishing, or data theft.

- Are explicitly designed for illegal activities or direct hacking that puts the repository at legal risk.

- Are empty repositories or applications with no real functionality (spam).

## 🔄 Update Process
Updates will be reflected in Aura Repo by tracking new releases in your repository. Just make sure you properly label your versions on GitHub, and we'll take care of the rest.

---

Does your app meet these simple requirements? Then we'd love to have it! Go to the [Issues](../../issues) section and open a new **App Request (RFP)**.
