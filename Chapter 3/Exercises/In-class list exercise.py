"""
Given the list of countries, find the country that has the longest name
including spaces.

Print the name of the country and how many characters there are in the name.
"""

countries = ['United States', 'Russia', 'Canada', 'China', 'Mexico', 'Brazil', 'Italy', 'United Kingdom', 'Australia',
             'France', 'Germany', 'Spain', 'Japan', 'India', 'Egypt', 'Ireland', 'Iceland', 'Argentina', 'South Africa',
             'Portugal', 'Sweden', 'Chile', 'Norway', 'South Korea', 'Finland', 'Turkey', 'North Korea', 'Greece',
             'Iran', 'New Zealand', 'Poland', 'Iraq', 'Denmark', 'Madagascar', 'Peru', 'Switzerland', 'Cuba',
             'Netherlands', 'Pakistan', 'Mongolia', 'Saudi Arabia', 'Indonesia', 'Colombia', 'Austria', 'Ukraine',
             'Belgium', 'Niger', 'Thailand', 'Afghanistan', 'Vietnam', 'Morocco', 'Israel', 'Panama',
             'Democratic Republic of the Congo', 'Uruguay', 'Bolivia', 'Sudan', 'Venezuela', 'Republic of the Congo',
             'Kazakhstan', 'Philippines', 'Nigeria', 'Romania', 'Hungary', 'Paraguay', 'Nepal', 'Czech Republic',
             'Croatia', 'Algeria', 'Syria', 'Libya', 'Estonia', 'Yemen', 'Slovakia', 'Kenya', 'Somalia', 'Haiti',
             'United Arab Emirates', 'Latvia', 'Ethiopia', 'Lithuania', 'Malaysia', 'Jamaica', 'Papua New Guinea',
             'Sri Lanka', 'Ecuador', 'Dominica', 'Chad', 'Oman', 'Belarus', 'Bulgaria', 'Laos', 'Cambodia', 'Albania',
             'Jordan', 'Taiwan', 'Serbia', 'Luxembourg', 'Slovenia', 'Costa Rica', 'Bosnia and Herzegovina',
             'Uzbekistan', 'Bangladesh', 'Tunisia', 'Zimbabwe', 'Honduras', 'Myanmar', 'Guatemala', 'Georgia', 'Ghana',
             'Mali', 'Dominican Republic', 'Vatican City', 'Bahamas', 'Cyprus', 'South Sudan', 'North Macedonia',
             'Turkmenistan', 'Nicaragua', 'Angola', 'Qatar', 'Singapore', 'Ivory Coast', 'Armenia', 'Lebanon', 'Belize',
             'Tanzania', 'Malta', 'Uganda', 'El Salvador', 'Zambia', 'Fiji', 'Andorra', 'Guinea', 'Guyana', 'Moldova',
             'Azerbaijan', 'Botswana', 'Monaco', 'Bhutan', 'Montenegro', 'Namibia', 'Central African Republic', 'Kuwait',
             'Mozambique', 'Liberia', 'Liechtenstein', 'Suriname', 'Kosovo', 'Cameroon', 'Senegal', 'Rwanda', 'Togo',
             'Tajikistan', 'Lesotho', 'Trinidad and Tobago', 'Eritrea', 'Kyrgyzstan', 'Barbados', 'Eswatini',
             'San Marino', 'Maldives', 'Mauritania', 'Gambia', 'Malawi', 'Benin', 'Sierra Leone', 'Bahrain', 'Mauritius',
             'Djibouti', 'Gabon', 'Federated States of Micronesia', 'Seychelles', 'Tonga', 'Brunei', 'Burkina Faso',
             'Samoa', 'Cape Verde', 'Burundi', 'Equatorial Guinea', 'East Timor', 'Antigua and Barbuda',
             'Solomon Islands', 'Saint Kitts and Nevis', 'Saint Lucia', 'Guinea-Bissau', 'Vanuatu', 'Marshall Islands',
             'Tuvalu', 'Grenada', 'Kiribati', 'Saint Vincent and the Grenadines', 'Palau', 'Comoros', 'Nauru', 'São Tomé and Príncipe']

longest_country = ""
longest_length = 0

for country in countries:
    if len(country) > longest_length:
        longest_length = len(country)
        # print(longest_length)
        longest_country = country

print(longest_country, longest_length)

countries.sort()
print(countries)