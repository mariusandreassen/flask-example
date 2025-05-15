import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { PlusCircle, Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

export default function CustomersPage() {
  const customers = [
    { id: "CUS001", name: "Globex Corporation", contact: "globex@example.com", type: "Enterprise", status: "Active" },
    { id: "CUS002", name: "Stark Industries", contact: "stark@example.com", type: "Corporate", status: "Active" },
    { id: "CUS003", name: "Wayne Enterprises", contact: "wayne@example.com", type: "Enterprise", status: "Inactive" },
  ];
  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row items-center justify-between gap-4">
        <h1 className="text-3xl font-bold tracking-tight">Customers</h1>
        <div className="flex items-center gap-2 w-full md:w-auto">
          <div className="relative flex-1 md:flex-initial">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input type="search" placeholder="Search customers..." className="pl-8 w-full md:w-[300px]" />
          </div>
          <Button>
            <PlusCircle className="mr-2 h-5 w-5" /> Add Customer
          </Button>
        </div>
      </div>
      
      <Card>
        <CardHeader>
          <CardTitle>Customer List</CardTitle>
          <CardDescription>Manage your company's customers.</CardDescription>
        </CardHeader>
        <CardContent>
           <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>Name</TableHead>
                <TableHead>Contact Email</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Actions</TableTableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {customers.map((cus) => (
                <TableRow key={cus.id}>
                  <TableCell className="font-medium">{cus.id}</TableCell>
                  <TableCell>{cus.name}</TableCell>
                  <TableCell>{cus.contact}</TableCell>
                  <TableCell>{cus.type}</TableCell>
                   <TableCell>
                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                      cus.status === "Active" ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200" : "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200"
                    }`}>
                      {cus.status}
                    </span>
                  </TableCell>
                  <TableCell>
                    <Button variant="outline" size="sm">View</Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
