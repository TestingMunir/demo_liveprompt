<<<<<<< HEAD
pipeline {
agent any


environment {
// Name of the automation container service from docker-compose.yml
AUTOMATION_SERVICE = "automation-tests"
}


stages {
stage('Checkout') {
steps {
// Pull the latest code from Git repository
checkout scm
}
}


stage('Start Selenium Grid') {
steps {
echo "Starting Selenium Hub + Chrome nodes..."
// Starts Selenium Hub and Chrome nodes in background
sh 'docker compose up -d selenium-hub selenium-chrome'
}
}


stage('Run Automation Tests') {
steps {
echo "Running automation tests container..."
// Start automation-tests service (from testing profile)
sh "docker compose --profile testing up --build --abort-on-container-exit ${AUTOMATION_SERVICE}"
}
}


stage('Collect Reports') {
steps {
echo "Archiving test reports, logs, and screenshots..."
// Archive test artifacts for Jenkins
archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
archiveArtifacts artifacts: 'logs/**/*', allowEmptyArchive: true
archiveArtifacts artifacts: 'screenshots/**/*', allowEmptyArchive: true
}
}
}


post {
always {
echo "Cleaning up Docker containers..."
sh 'docker compose down'
}
}
=======
pipeline {
agent any


environment {
// Name of the automation container service from docker-compose.yml
AUTOMATION_SERVICE = "automation-tests"
}


stages {
stage('Checkout') {
steps {
// Pull the latest code from Git repository
checkout scm
}
}


stage('Start Selenium Grid') {
steps {
echo "Starting Selenium Hub + Chrome nodes..."
// Starts Selenium Hub and Chrome nodes in background
sh 'docker compose up -d selenium-hub selenium-chrome'
}
}


stage('Run Automation Tests') {
steps {
echo "Running automation tests container..."
// Start automation-tests service (from testing profile)
sh "docker compose --profile testing up --build --abort-on-container-exit ${AUTOMATION_SERVICE}"
}
}


stage('Collect Reports') {
steps {
echo "Archiving test reports, logs, and screenshots..."
// Archive test artifacts for Jenkins
archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
archiveArtifacts artifacts: 'logs/**/*', allowEmptyArchive: true
archiveArtifacts artifacts: 'screenshots/**/*', allowEmptyArchive: true
}
}
}


post {
always {
echo "Cleaning up Docker containers..."
sh 'docker compose down'
}
}
>>>>>>> df94acca538cdf2652acf94a96c6d47eb8d9e940
}