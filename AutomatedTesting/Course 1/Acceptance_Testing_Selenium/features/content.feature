Feature: Test that pages have correct content
    Scenario: Blog page has a correct title
        Given I am on the blog page
        Then Page has a title
        And Page has the title "This is the blog page"

    Scenario: Home page has a correct title
        Given I am on the homepage
        Then Page has a title
        And Page has the title "This is the homepage"
