from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>CCIT DevOps Platform</title>

        <style>

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: #f5f7fb;
                color: #1f2937;
            }

            /* =========================
               HEADER
            ========================== */

            header {
                height: 70px;
                background: #111827;
                color: white;

                display: flex;
                align-items: center;
                justify-content: space-between;

                padding: 0 50px;

                box-shadow: 0 3px 15px rgba(0,0,0,0.15);
            }

            .logo {
                display: flex;
                align-items: center;
                gap: 12px;

                font-size: 22px;
                font-weight: bold;
            }

            .logo-icon {
                width: 40px;
                height: 40px;

                background: #2563eb;

                border-radius: 10px;

                display: flex;
                align-items: center;
                justify-content: center;

                font-size: 20px;
            }

            .status {
                display: flex;
                align-items: center;
                gap: 8px;

                font-size: 14px;
                color: #d1d5db;
            }

            .status-dot {
                width: 10px;
                height: 10px;

                background: #22c55e;

                border-radius: 50%;

                box-shadow: 0 0 10px #22c55e;
            }


            /* =========================
               HERO SECTION
            ========================== */

            .hero {
                background: linear-gradient(
                    135deg,
                    #111827,
                    #1e3a8a
                );

                color: white;

                padding: 70px 50px;

                position: relative;
                overflow: hidden;
            }

            .hero::before {
                content: "";

                position: absolute;

                width: 350px;
                height: 350px;

                background: rgba(59,130,246,0.2);

                border-radius: 50%;

                right: -100px;
                top: -150px;
            }

            .hero-content {
                max-width: 1100px;
                margin: auto;

                position: relative;
                z-index: 2;
            }

            .badge {
                display: inline-block;

                background: rgba(255,255,255,0.12);

                padding: 8px 15px;

                border-radius: 20px;

                font-size: 13px;

                margin-bottom: 20px;
            }

            .hero h1 {
                font-size: 48px;

                margin-bottom: 15px;

                letter-spacing: -1px;
            }

            .hero p {
                font-size: 18px;

                color: #dbeafe;

                max-width: 700px;

                line-height: 1.6;
            }


            /* =========================
               MAIN CONTENT
            ========================== */

            .container {
                max-width: 1100px;

                margin: -30px auto 50px;

                padding: 0 25px;

                position: relative;
                z-index: 5;
            }


            /* =========================
               CARDS
            ========================== */

            .cards {
                display: grid;

                grid-template-columns:
                    repeat(3, 1fr);

                gap: 20px;
            }

            .card {
                background: white;

                border-radius: 15px;

                padding: 25px;

                box-shadow:
                    0 8px 30px rgba(0,0,0,0.08);

                border: 1px solid #e5e7eb;

                transition: all 0.3s ease;
            }

            .card:hover {
                transform: translateY(-6px);

                box-shadow:
                    0 15px 35px rgba(0,0,0,0.12);
            }

            .card-icon {
                width: 50px;
                height: 50px;

                border-radius: 12px;

                background: #eff6ff;

                display: flex;
                align-items: center;
                justify-content: center;

                font-size: 24px;

                margin-bottom: 18px;
            }

            .card h3 {
                font-size: 18px;

                margin-bottom: 8px;
            }

            .card p {
                color: #6b7280;

                font-size: 14px;

                line-height: 1.6;
            }


            /* =========================
               INFORMATION SECTION
            ========================== */

            .section {
                margin-top: 35px;

                background: white;

                padding: 30px;

                border-radius: 15px;

                box-shadow:
                    0 8px 30px rgba(0,0,0,0.06);

                border: 1px solid #e5e7eb;
            }

            .section-title {
                font-size: 22px;

                margin-bottom: 25px;
            }

            .info-grid {
                display: grid;

                grid-template-columns:
                    repeat(2, 1fr);

                gap: 15px;
            }

            .info-item {
                background: #f9fafb;

                padding: 18px;

                border-radius: 10px;

                border-left: 4px solid #2563eb;
            }

            .info-label {
                font-size: 12px;

                color: #6b7280;

                text-transform: uppercase;

                letter-spacing: 1px;

                margin-bottom: 5px;
            }

            .info-value {
                font-size: 16px;

                font-weight: bold;

                color: #111827;
            }


            /* =========================
               PIPELINE
            ========================== */

            .pipeline {
                display: flex;

                align-items: center;

                justify-content: space-between;

                margin-top: 20px;

                gap: 10px;
            }

            .pipeline-step {
                flex: 1;

                text-align: center;
            }

            .pipeline-icon {
                width: 55px;
                height: 55px;

                margin: auto;

                background: #2563eb;

                color: white;

                border-radius: 50%;

                display: flex;
                align-items: center;
                justify-content: center;

                font-size: 20px;

                margin-bottom: 10px;
            }

            .pipeline-step strong {
                display: block;

                font-size: 14px;

                margin-bottom: 4px;
            }

            .pipeline-step span {
                font-size: 12px;

                color: #6b7280;
            }

            .arrow {
                font-size: 25px;

                color: #9ca3af;
            }


            /* =========================
               FOOTER
            ========================== */

            footer {
                background: #111827;

                color: #9ca3af;

                text-align: center;

                padding: 25px;

                font-size: 13px;
            }

            footer strong {
                color: white;
            }


            /* =========================
               RESPONSIVE
            ========================== */

            @media (max-width: 800px) {

                header {
                    padding: 0 20px;
                }

                .hero {
                    padding: 50px 25px;
                }

                .hero h1 {
                    font-size: 34px;
                }

                .cards {
                    grid-template-columns: 1fr;
                }

                .info-grid {
                    grid-template-columns: 1fr;
                }

                .pipeline {
                    flex-direction: column;
                }

                .arrow {
                    transform: rotate(90deg);
                }
            }

        </style>
    </head>

    <body>


        <!-- =========================
             HEADER
        ========================== -->

        <header>

            <div class="logo">

                <div class="logo-icon">
                    ☁
                </div>

                CCIT DevOps

            </div>


            <div class="status">

                <span class="status-dot"></span>

                Application Online

            </div>

        </header>



        <!-- =========================
             HERO
        ========================== -->

        <section class="hero">

            <div class="hero-content">

                <div class="badge">
                    Kubernetes Deployment
                </div>

                <h1>
                    Cloud Computing in Telugu
                </h1>

                <p>
                    Welcome to the CCIT Kubernetes Demo3 application.
                    This application is deployed using Docker,
                    Kubernetes and Argo CD GitOps.
                </p>

            </div>

        </section>



        <!-- =========================
             MAIN
        ========================== -->

        <main class="container">


            <!-- SERVICE CARDS -->

            <div class="cards">


                <div class="card">

                    <div class="card-icon">
                        ☸️
                    </div>

                    <h3>
                        Kubernetes
                    </h3>

                    <p>
                        Application is running inside a Kubernetes
                        cluster with multiple replicas for
                        high availability.
                    </p>

                </div>



                <div class="card">

                    <div class="card-icon">
                        🚀
                    </div>

                    <h3>
                        Argo CD
                    </h3>

                    <p>
                        Continuous deployment is managed through
                        GitOps using Argo CD.
                    </p>

                </div>



                <div class="card">

                    <div class="card-icon">
                        🐳
                    </div>

                    <h3>
                        Docker
                    </h3>

                    <p>
                        The application is packaged as a Docker
                        container and stored in Docker Hub.
                    </p>

                </div>


            </div>



            <!-- APPLICATION INFORMATION -->

            <section class="section">

                <h2 class="section-title">
                    Application Information
                </h2>


                <div class="info-grid">


                    <div class="info-item">

                        <div class="info-label">
                            Application
                        </div>

                        <div class="info-value">
                            CCIT - Demo3
                        </div>

                    </div>



                    <div class="info-item">

                        <div class="info-label">
                            Platform
                        </div>

                        <div class="info-value">
                            Kubernetes
                        </div>

                    </div>



                    <div class="info-item">

                        <div class="info-label">
                            Deployment
                        </div>

                        <div class="info-value">
                            Argo CD GitOps
                        </div>

                    </div>



                    <div class="info-item">

                        <div class="info-label">
                            Container Port
                        </div>

                        <div class="info-value">
                            5000
                        </div>

                    </div>


                </div>

            </section>



            <!-- DEPLOYMENT PIPELINE -->

            <section class="section">

                <h2 class="section-title">
                    Deployment Pipeline
                </h2>


                <div class="pipeline">


                    <div class="pipeline-step">

                        <div class="pipeline-icon">
                            📦
                        </div>

                        <strong>
                            GitHub
                        </strong>

                        <span>
                            Source Code
                        </span>

                    </div>


                    <div class="arrow">
                        →
                    </div>


                    <div class="pipeline-step">

                        <div class="pipeline-icon">
                            🔨
                        </div>

                        <strong>
                            GitHub Actions
                        </strong>

                        <span>
                            Build & Push
                        </span>

                    </div>


                    <div class="arrow">
                        →
                    </div>


                    <div class="pipeline-step">

                        <div class="pipeline-icon">
                            🐳
                        </div>

                        <strong>
                            Docker Hub
                        </strong>

                        <span>
                            Container Image
                        </span>

                    </div>


                    <div class="arrow">
                        →
                    </div>


                    <div class="pipeline-step">

                        <div class="pipeline-icon">
                            ☸️
                        </div>

                        <strong>
                            Kubernetes
                        </strong>

                        <span>
                            Application
                        </span>

                    </div>


                    <div class="arrow">
                        →
                    </div>


                    <div class="pipeline-step">

                        <div class="pipeline-icon">
                            🔄
                        </div>

                        <strong>
                            Argo CD
                        </strong>

                        <span>
                            GitOps Sync
                        </span>

                    </div>


                </div>

            </section>


        </main>



        <!-- =========================
             FOOTER
        ========================== -->

        <footer>

            <strong>
                Cloud Computing in Telugu
            </strong>

            &nbsp; | &nbsp;

            Kubernetes Demo

            <br><br>

            Built with Flask • Docker • Kubernetes • Argo CD by CCIT

        </footer>


    </body>

    </html>
    """

PASSWORD= "123456"
PASSWORD= "1234567"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )