# Create Dictionary
# Create TestPassfile
```zsh
echo -n 'ABC123chocolate!!!' | sha256sum | awk '{print $1}' > hash.txt
```
![](../../../Assets/Images/Pasted%20image%2020260502125122.png)

# Create Dictionary
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```

![](../../../Assets/Images/Pasted%20image%2020260502124644.png)

# Crack
```zsh
 hashcat -a 0 -m 1400 hash.txt rockyou_hybrid.txt
```
![](../../../Assets/Images/Pasted%20image%2020260502125609.png)
![](../../../Assets/Images/Pasted%20image%2020260502125544.png)