// plugins {
//     java
// }

// repositories {
//     mavenCentral()
// }

// dependencies {
//     testImplementation("org.seleniumhq.selenium:selenium-java:4.20.0")
//     testImplementation("org.testng:testng:7.9.0")
//     testImplementation("io.github.bonigarcia:webdrivermanager:5.7.0")
// }

// tasks.test {
//     useTestNG()
// }
// plugins {
//     id 'java'
// }

// repositories {
//     mavenCentral()
// }

// dependencies {
//     // TestNG dependency
//     testImplementation 'org.testng:testng:7.8.0'
    
//     // If using Selenium for Web automation
//     implementation 'org.seleniumhq.selenium:selenium-java:4.15.0'
    
//     // If using Appium for mobile automation
//     implementation 'io.appium:java-client:8.6.0'
// }

// test {
//     useTestNG() {
//         // TestNG configuration
//         suites 'src/test/resources/testng.xml'
//     }
// }


plugins {
    id 'java'
}

group = 'com.yourcompany'
version = '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    // Test Framework
    testImplementation 'org.testng:testng:7.9.0'
    
    // Selenium for Web Automation
    testImplementation 'org.seleniumhq.selenium:selenium-java:4.20.0'
    
    // WebDriver Manager for automatic driver management
    testImplementation 'io.github.bonigarcia:webdrivermanager:5.7.0'
    
    // Appium for Mobile Automation
    testImplementation 'io.appium:java-client:9.0.0'
    
    // For logging
    testImplementation 'org.slf4j:slf4j-simple:2.0.13'
    
    // For reading config files (optional)
    testImplementation 'com.fasterxml.jackson.core:jackson-databind:2.16.1'
    testImplementation 'com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.16.1'
}

test {
    useTestNG() {
        // Use testng.xml if present
        if (file('src/test/resources/testng.xml').exists()) {
            suites 'src/test/resources/testng.xml'
        }
        // OR use include groups
        // includeGroups 'smoke'
        
        useDefaultListeners = true
    }
    
    testLogging {
        events "passed", "skipped", "failed", "standardOut", "standardError"
        showStandardStreams = true
    }
    
    // Run tests in parallel (optional)
    maxParallelForks = 3
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}