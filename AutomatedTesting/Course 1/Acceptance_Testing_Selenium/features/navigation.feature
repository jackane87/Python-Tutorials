Feature: Test navigation between pages

    Longer descriptions can be added below the feature title.

    Scenario: Homepage can go to the Blog
        Given I am on the homepage
        When I click on the link with id "blog-link"
        Then I am on the blog page

    Scenario: Blog can go to the Homepage
        Given I am on the blog page
        When I click on the link with id "home-link"
        Then I am on the homepage

