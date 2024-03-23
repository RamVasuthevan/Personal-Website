---
layout: page
title: Git Scraping
---

Inspired by [Simon Willison](https://simonwillison.net/2020/Oct/9/git-scraping/). 

Download a file regularly using Git Actions, check it into Git and see how it changes over time.

### Scraping Project
<table>
  <tbody>
    <tr>
      <td><strong>Projects</strong></td>
      <td><strong>Notes</strong></td>
      <td><strong>Updated</strong></td>
    </tr>
    {% for project in site.data.git-scraping %}
    <tr>
      <td><a href="{{project.name_url}}" target="_blank">{{project.name}}</a></td>
      <td>
        <ul>
          {% for note in project.notes %}
          <li>{{ note | markdownify | remove: '<p>' | remove: '</p>' | replace: '<a ', '<a target="_blank" ' }}</li>
          {% endfor %}
        </ul>
      </td>
      <td>{{ project.updated | markdownify | remove: '<p>' | remove: '</p>' | replace: '<a ', '<a target="_blank" ' }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>


Future scraping pages:
- [Building Permits Cleared Permits—City of Toronto](https://open.toronto.ca/dataset/building-permits-cleared-permits/)
- [Building Permits Active Permits—City of Toronto](https://open.toronto.ca/dataset/building-permits-active-permits/)
- [Building Construction Demolition Violations—City of Toronto](https://open.toronto.ca/dataset/building-construction-demolition-violations/)
- [Apartment Building Evaluation—City of Toronto](https://open.toronto.ca/dataset/apartment-building-evaluation/)
- [Traffic Volumes at Intersections for All Modes—City of Toronto](https://open.toronto.ca/dataset/traffic-volumes-at-intersections-for-all-modes/)
- [Highrise Residential Fire Inspection Results—City of Toronto](https://open.toronto.ca/dataset/highrise-residential-fire-inspection-results/)
- [DineSafe—City of Toronto](https://open.toronto.ca/dataset/dinesafe/)
- [Municipal Licensing and Standards Business Licences and Permits—City of Toronto](https://open.toronto.ca/dataset/municipal-licensing-and-standards-business-licences-and-permits/)
- [.nyc Domain Registrations—City of NYC](https://data.cityofnewyork.us/Business/-nyc-Domain-Registrations/9cw8-7heb/about_data)
- [City Record Online—City of NYC](https://data.cityofnewyork.us/City-Government/City-Record-Online/dg92-zbpx/about_data)

TODO: 
  - Create [Github: template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
