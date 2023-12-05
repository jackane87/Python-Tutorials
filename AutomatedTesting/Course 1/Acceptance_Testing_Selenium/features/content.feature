Feature: Test that pages have correct content
    Scenario: Blog page has a correct title
        Given I am on the blog page
        Then Page has a title
        And Page has the title "This is the blog page"
